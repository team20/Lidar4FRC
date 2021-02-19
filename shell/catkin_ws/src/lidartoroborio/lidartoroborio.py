#!/usr/bin/env python3
import rospy
import networktables
import math
from geometry_msgs.msg import PoseWithCovarianceStamped
from networktables import NetworkTables
def callback(data):
	quat = data.pose.pose.orientation
	rospy.loginfo("Position: x=%f y=%f z=%f th=%f", quat.x, quat.y, quat.z, quat.w)
	x.setDouble(quat.x)
	y.setDouble(quat.y)
	z.setDouble(quat.z)
	th.setDouble(quat.w)
def listener():
	rospy.init_node('lidartoroborio', anonymous=True)
	rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callback)
	NetworkTables.initialize(server="10.2.2.2")
	odom_table = NetworkTables.getTable("ODOMETRY")
	global x 
	x = odom_table.getEntry("LidarX")
	global y 
	y = odom_table.getEntry("LidarY")
	global z 
	z = odom_table.getEntry("LidarZ")
	global th 
	th = odom_table.getEntry("LidarTh")
	rospy.spin()

if __name__ == "__main__":
	listener()
