#!/usr/bin/env python3
import rospy
import networktables
import math
from sensor_msgs.msg import LaserScan
from networktables import NetworkTables


def callback(data):
    cart_pts = []
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ranges = data.ranges
    min = data.angle_min
    max = data.angle_max
    ang_incr = data.angle_increment
    for i in ranges:
        x = (i*math.cos(min))*3.28084
        y = (i*math.sin(min))*3.28084
        min += ang_incr
        if (y <= 3.75 and y >= -3.75) and (x <= 7.5 and x >= 0) and ((min >= (3*math.pi)/2) or (min <= math.pi/2)):
            x *= 2
            x = int(round(x))
            y *= 2
            y = int(round(y)) + 8
            grid[x][y] = 1
    byte = []
    bit = '0b0'
    boolGrid = []
    grid[0][8] = 0;
    for i in grid:
        print(i)
        for j in i:
            boolGrid.append(j == 1)
    g.setBooleanArray(boolGrid)
    print("\n")
def listener():
    rospy.init_node('ranges', anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    NetworkTables.initialize(server="10.0.20.2")
    odom_table = NetworkTables.getTable("ODOMETRY")
    global g
    g = odom_table.getEntry("grid")
    rospy.spin()

if __name__ == "__main__":
    listener()
