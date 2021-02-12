#!/usr/bin/env python3
import rospy
import networktables
import math
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(data):
	quat = data.pose.pose.orientation
	rospy.loginfo("Position: x=%f y=%f z=%f th=%f", quat.x, quat.y, quat.z, quat.w)
	
def listener():
	rospy.init_node('lidartoroborio', anonymous=True)
	rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callback)
	rospy.spin()

if __name__ == "__main__":
	listener()
