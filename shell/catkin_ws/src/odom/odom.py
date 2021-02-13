#!/usr/bin/env python3
import rospy
import networktables
import math
import tf
from tf import TransformBroadcaster
from nav_msgs.msg import Odometry
from networktables import NetworkTables
from geometry_msgs.msg import Quaternion, TransformStamped
def publisher():
	rospy.init_node('odom', anonymous=True)
	NetworkTables.initialize(server='roborio-20-frc.local')
	odom = NetworkTables.getTable('wheelodometry')
	rospy.Publisher('odom', Odometry, queue_size=1000)
	rate = rospy.Rate(100)
	odom_broadcaster = new TransformBroadcaster()
	while rospy.ok():
		currTime = rospy.Time.now()
		x = odom.getNumber('RobotX')
		y = odom.getNumber('RobotY')
		th = odom.getNumber('RobotTh')
		odom_quat = tf.createQuaternionMsgFromYaw(th)
		odom_trans = new TransformStamped()
		odom_trans.header.stamp = currTime
		odom_trans.header.frame_id = "odom"
		odom_trans.child_frame_id - "base_link"
		odom_trans.transform.translation.x = x
		odom_trans.transform.translation.y = y
		odom_trans.transform.translation.z = z
		odom_trans.transform.rotation = odom_quat
		odom_broadcaster.sendTransform(odom_trans)
		odom = new Odometry()
		odom.header.stamp = currTime
		odom.header.frame_id = "odom"
		odom.pose.position.x = x
		odom.pose.position.y = y
		odom.pose.position.z = 0.0
		odom.pose.pose.orientation = odom_quat
		odom.child_frame_id = "base_link"
		

if __name__ == "__main__":
	publisher()
