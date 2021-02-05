echo "Setting up ros"
source $ROS_HOME/setup.sh
catkin_make
echo "Setting up catkin workspace"
source $CATKIN_WS_HOME/devel/setup.bash
roslaunch start runsim.launch
