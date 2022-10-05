#! /home/singh/.virtualenvs/cv/bin/python

import pickle
import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
 
with open('/home/singh/ros_workspaces/parking_ws/src/Bvp_Galat_Family/parking_detector/scripts/CarParkPos', 'rb') as f:
    posList = pickle.load(f)
 

width, height = 90, 160
rospy.init_node("parking_detector")
img_bridge = CvBridge()
img_pub = rospy.Publisher("parking_detected_img", Image, queue_size=10)


def checkParkingSpace(imgPro, cv_img):
    spaceCounter = 0
 
    for pos in posList:
        x, y = pos
 
        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        if count < 3000:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
 
        cv_img = cv2.rectangle(cv_img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        ros_img = img_bridge.cv2_to_imgmsg(cv_img, encoding="bgr8")
        img_pub.publish(ros_img)
    
 
def image_cb(img):
    try:
        cv_image = img_bridge.imgmsg_to_cv2(img, desired_encoding="bgr8")
    except CvBridgeError:
        rospy.logerr("pipe_counter: ERROR IN RECEIVING IMAGE")

    imgGray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate, cv_image)


if __name__ == "__main__":
    img_sub = rospy.Subscriber("/iris/camera/image_raw", Image, image_cb)

    rospy.spin()
    cv2.waitKey(0)