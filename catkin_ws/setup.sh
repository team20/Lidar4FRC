echo "Setting up ros"
source $ROS_HOME/setup.sh
echo "Setting up catkin workspace"
source $CATKIN_WS_HOME/devel/setup.bash
#roslaunch start run.launch
roslaunch ydlidar_ros gazebo.launch
