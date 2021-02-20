if [ ! -f "./.ros_built" ] || [ "$1" = "-rebuild" ]; then
	docker build -t ros . && touch .ros_built
fi
#docker build -t ros .
docker stop ros_build
docker rm ros_build
if [ ! -f /dev/ttyUSB0 ]; then
	docker run -itd --device=/dev/ttyUSB0 --mount type=bind,source="/home/pi/rosvision/shell/catkin_ws",target="/home/catkin_ws" --name=ros_build ros
else
	echo "no lidar detected"
fi
