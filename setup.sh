sudo docker build -t ros .
sudo docker run -it --device=/dev/ttyUSB0 ros bash
