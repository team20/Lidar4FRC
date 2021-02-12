FROM ubuntu:18.04
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN date
RUN apt-get update
RUN apt-get install -y gnupg
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y ros-melodic-ros-base 
RUn apt-get install -y ros-melodic-amcl ros-melodic-tf ros-melodic-map-server ros-melodic-slam-gmapping
RUN apt-get install -y git
RUN apt-get install -y g++
RUN apt-get install -y python3-pip
RUN pip3 install pynetworktables
RUN pip3 install pyyaml
RUN pip3 install rospkg 
RUN apt-get install -y nano
CMD . /opt/ros/melodic/setup.sh && cd /home/catkin_ws && ls && catkin_make && ln -s /dev/ttyUSB0 /dev/ydlidar && bash
