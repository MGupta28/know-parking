#! /usr/bin/python

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from parking_detector.msg import Booking


class Robot_Controller:
    #initialised values
    def __init__(self):

        rospy.init_node('Move_Joint')
        self.pub = rospy.Publisher('/servo', UInt16, queue_size=10)
        self.pub2 = rospy.Publisher('/lcd', String, queue_size=10)

        rospy.Subscriber('/parking_booking', Booking, self.Book_cb)
            
    
    def Book_cb(self, data):
        self.pub2.publish(str(data.parking_space))
        #self.pub.publish(120)
        



if __name__ == "__main__":
    Robot = Robot_Controller()
    rospy.spin()