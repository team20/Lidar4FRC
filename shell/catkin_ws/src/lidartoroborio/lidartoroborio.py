#!/usr/bin/env python3
import rospy
import networktables
import math
from geometry_msgs.msg import PoseWithCovarianceStamped
from networktables import NetworkTables
#def callback(data):
	#quat = data.pose.pose.orientation
	#pos = data.pose.pose.position
	#rospy.loginfo("Position: x=%f y=%f z=%f th=%f", pos.x, pos.y, pos.z, quat.w)
	#rospy.loginfo("debug")
	#x.setDouble(1000)
	#y.setDouble(123213)
	#z.setDouble(483483)
	#th.setDouble(2938)
#def listener():
	#rospy.init_node('lidartoroborio', anonymous=True)
	#rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callback)
	#NetworkTables.initialize(server="10.0.20.136")
	#odom_table = NetworkTables.getTable("ODOMETRY")
	#global x 
	#x = odom_table.getEntry("LidarX")
	#global y 
	#y = odom_table.getEntry("LidarY")
	#global z 
	#z = odom_table.getEntry("LidarZ")
	#global th 
	#th = odom_table.getEntry("LidarTh")
#	rospy.spin()

#if __name__ == "__main__":
#	listener()
