#!/usr/bin/env python3
import rospy
import networktables
import math
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(data):
	rospy.loginfo("Range: %f", data.pose.pose.position.x)
	
def listener():
	rospy.init_node('lidartoroborio', anonymous=True)
	rospy.Subscriber('odom', PoseWithCovarianceStamped, callback)
	rospy.spin()

if __name__ == "__main__":
	listener()
