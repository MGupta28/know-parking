#! /bin/zsh

source /usr/share/gazebo/setup.bash
export GAZEBO_MODEL_PATH="${CATKIN_ENV_HOOK_WORKSPACE}/../src/know_parking/parking_sim/models/:${GAZEBO_MODEL_PATH}"
export GAZEBO_RESOURCE_PATH="${CATKIN_ENV_HOOK_WORKSPACE}/../src/know_parking/parking_sim/models/:${CATKIN_ENV_HOOK_WORKSPACE}/../src/parking_sim/worlds/:${GAZEBO_RESOURCE_PATH}"

