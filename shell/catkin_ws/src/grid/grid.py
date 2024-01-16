#!/usr/bin/env python3
import rospy
import networktables
import math
from sensor_msgs.msg import LaserScan
from networktables import NetworkTables

prev_times = []

def callback(data):
    cart_pts = []
    ranges = data.ranges
    min = data.angle_min
    max = data.angle_max
    ang_incr = data.angle_increment

    for i, r in enumerate(ranges):
        current_angle = 180 + int((i * ang_incr + min) * 180.0 / 3.141592)
        if not (((current_angle % 45) == 0) or ((current_angle % 30) == 0)):
           continue
        if ((r < 0.5) or (r > 8.5)):
           continue #r = 0
        print(str(current_angle), "   :   ", r)
        sd.putNumber(str(current_angle), round(r,4))

    sd.putNumber(str(min), 389)
def listener():
    rospy.init_node('ranges', anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    NetworkTables.initialize(server="10.0.20.2")
    global sd
    sd = NetworkTables.getTable('SmartDashboard')

    #sd.putNumber('someNumber', 9)

    odom_table = NetworkTables.getTable("ODOMETRY")
    global g
    g = odom_table.getEntry("grid")
    rospy.spin()

if __name__ == "__main__":
    listener()
