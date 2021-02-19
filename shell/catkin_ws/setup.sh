#!/usr/bin/env bash

echo "Setting up ros"
source /opt/ros/melodic/setup.sh
catkin_make
echo "Setting up catkin workspace"
source /home/catkin_ws/devel/setup.bash
echo "Launching ROS"
roslaunch start run.launch
