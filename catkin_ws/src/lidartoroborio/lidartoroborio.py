#!/usr/bin/env python3
import rospy
import networktables
import math
from sensor_msgs.msg import LaserScan

def callback(data):
	rospy.loginfo("Range: %f, %f", data.angle_min*(180/math.pi), data.angle_max*(180/math.pi))
	
def listener():
	rospy.init_node('lidartoroborio', anonymous=True)
	rospy.Subscriber('scan', LaserScan, callback)
	rospy.spin()

if __name__ == "__main__":
	listener()
