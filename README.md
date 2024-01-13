# rosvision
1. Install Docker on the pi by running get-docker.sh
2. run ./setup.sh to start everything up\

\
Directory Structure:\
shell/catkin_ws has everything. There's a lot going on there, but the only file you really need to worry about\
is shell/catkin_ws/src/lidartoroborio/lidartoroborio.py, as that is where the data is actually published to the roborio\
using network tables.\
Also\
shell/catkin_ws/src/grid/grid.py reads messages from the "scan" topic and uses them to build an occupancy grid.\
While this may not be directly useful, it can serve as a guide for who to read from the scan topic and output to\
a network table.
