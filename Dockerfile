FROM ubuntu:20.04
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y gnupg
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y ros-noetic-ros-base ros-noetic-amcl
RUN apt-get install -y ros-noetic-tf
RUN apt-get install -y git
RUN apt-get install -y g++
RUN apt-get install -y python3-pip
RUN apt-get install -y ros-noetic-map-server
RUN pip3 install pynetworktables
RUN ln -s /dev/ttyUSB0 /dev/ydlidar
ADD ./shell /home

ENTRYPOINT /bin/bash
