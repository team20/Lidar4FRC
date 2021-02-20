#!/usr/bin/env python2
import rospy
import networktables
import math
import tf
from tf import TransformBroadcaster
from nav_msgs.msg import Odometry
from networktables import NetworkTables
from networktables import NetworkTablesInstance
from geometry_msgs.msg import Quaternion, TransformStamped
def publisher():
	rospy.init_node('odom', anonymous=True)
	NetworkTables.initialize(server='10.0.20.2')
	odom_table = NetworkTables.getTable('ODOMETRY')
	odom_pub = rospy.Publisher('odom', Odometry, queue_size=1000)
	r = rospy.Rate(100)
	odom_broadcaster = TransformBroadcaster()
	while not rospy.is_shutdown():
		currTime = rospy.Time.now()
		x = odom_table.getNumber('driveX', 0)
		y = odom_table.getNumber('driveY', 0)
		th = odom_table.getNumber('driveTh', 0)
		vx = odom_table.getNumber('driveVX', 0)
		vy = odom_table.getNumber('driveVY', 0)
		vth = odom_table.getNumber('driveVTh', 0)
		q = tf.transformations.quaternion_from_euler(0,0,th)
		odom_quat = Quaternion(*q)
		odom_trans = TransformStamped()
		odom_trans.header.stamp = currTime
		odom_trans.header.frame_id = "odom"
		odom_trans.child_frame_id = "base_link"
		odom_trans.transform.translation.x = x
		odom_trans.transform.translation.y = y
		odom_trans.transform.translation.z = 0
		odom_trans.transform.rotation = odom_quat
		odom_broadcaster.sendTransformMessage(odom_trans)
		odom = Odometry()
		odom.header.stamp = currTime
		odom.header.frame_id = "odom"
		odom.pose.pose.position.x = x
		odom.pose.pose.position.y = y
		odom.pose.pose.position.z = 0.0
		odom.pose.pose.orientation = odom_quat
		odom.child_frame_id = "base_link"
		odom.twist.twist.linear.x = vx
		odom.twist.twist.linear.y = vy
		odom.twist.twist.angular.z = vth
		odom_pub.publish(odom)
		r.sleep()

if __name__ == "__main__":
	publisher()
