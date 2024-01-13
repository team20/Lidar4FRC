# rosvision
1. Install Docker on the pi by running get-docker.sh
2. run ./setup.sh to start everything up\

\
Directory Structure:\
shell/catkin_ws has everything. There's a lot going on there, but the only file you really need to worry about\
is shell/catkin_ws/src/lidartoroborio/lidartoroborio.py, as that is where the data is actually published to the roborio\
using network tables.
