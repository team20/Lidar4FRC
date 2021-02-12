if [ -f "./.ros_built"]; then
	docker build ros
fi
docker run -itd --device=/dev/ttyUSB0 --mount type=bind,source="./shell/catkin_ws",target="/home/catkin_ws" ros
