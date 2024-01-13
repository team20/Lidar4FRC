#!/usr/bin/env python3
import rospy
import networktables
import math
from sensor_msgs.msg import LaserScan
from networktables import NetworkTables

#What a LaserScan message looks like
#This becomes 'data' (sorry for the bad name) in the callback function


'''
# Single scan from a planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

Header header            # timestamp in the header is the acquisition time of 
                         # the first ray in the scan.
                         #
                         # in frame frame_id, angles are measured around 
                         # the positive Z axis (counterclockwise, if Z is up)
                         # with zero angle being forward along the x axis
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities    # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.
'''


def callback(data):
	#works as a printf basically
	rospy.loginfo("Position: x=%f y=%f z=%f th=%f", pos.x, pos.y, pos.z, quat.w)
	#
	# figure out min distance from scan
	#
	min_distance.setDouble({min distance})
	th.setDouble({min angle})
	
def listener():
	rospy.init_node('lidartoroborio', anonymous=True)
	rospy.Subscriber('scan', LaserScan, callback)
	NetworkTables.initialize(server="10.2.2.2") #Make sure to set this to the right IP
	lidar_table = NetworkTables.getTable("LIDAR")
	global x 
	min_distance = lidar_table.getEntry("LidarMinRange")
	th = lidar_table.getEntry("LidarMinRangeAngle")
	rospy.spin()

if __name__ == "__main__":
	listener()
