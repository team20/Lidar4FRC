if [ ! -f "./.ros_built" ]; then
	docker build -t ros .
fi
docker run -itd --device=/dev/ttyUSB0 --mount type=bind,source="/home/pi/rosvision/shell/catkin_ws",target="/home/catkin_ws" --name=ros_build ros
