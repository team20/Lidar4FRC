cmake_minimum_required(VERSION 2.8.3)
project(test)

find_package(catkin REQUIRED COMPONENTS
  rosconsole
  roscpp
  std_msgs
)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(talker talker.cpp)
target_link_libraries(talker
   ${catkin_LIBRARIES} 
)
add_executable(listener listener.cpp)
target_link_libraries(listener
   ${catkin_LIBRARIES} 
 )
