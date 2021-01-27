cmake_minimum_required(VERSION 2.8.3)
project(sim)

find_package(catkin REQUIRED COMPONENTS
  rosconsole
  roscpp
  nav_msgs
  tf
)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(odom odom.cpp)
target_link_libraries(odom
   ${catkin_LIBRARIES} 
)
add_executable(lidar lidar.cpp)
target_link_libraries(lidar
   ${catkin_LIBRARIES} 
)
