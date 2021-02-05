echo "Setting up ros"
source /opt/ros/noetic/setup.sh
catkin_make
echo "Setting up catkin workspace"
source ./devel/setup.bash
roslaunch start run.launch
