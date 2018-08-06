#!/usr/bin/env python2
import rospy
from std_msgs.msg import Bool, Int16

def estop(msg):
    global stopped
    stopped = msg.data != 0

def vl1(msg):
    global distance
    distance[0] = msg.data
def vl2(msg):
    global distance
    distance[1] = msg.data
def vl3(msg):
    global distance
    distance[2] = msg.data
def vl4(msg):
    global distance
    distance[3] = msg.data
def vl5(msg):
    global distance
    distance[4] = msg.data
def vl6(msg):
    global distance
    distance[5] = msg.data
def cb(event):
    global stopped
    if stopped:
        print(distance)
        if sum(distance) == 255*6:
            stopped=False
            ePub.publish(Int16(0))

global stopped
stopped=False
distance = [0,0,0,0,0,0]
rospy.init_node("estop_mgr")
ePub = rospy.Publisher("/platform/e_stop", Int16, queue_size=3)
rospy.Subscriber("/platform/e_stop", Int16, estop)
rospy.Subscriber("/platform/distance/lf", Int16, vl1)
rospy.Subscriber("/platform/distance/lr", Int16, vl2)
rospy.Subscriber("/platform/distance/rf", Int16, vl3)
rospy.Subscriber("/platform/distance/rr", Int16, vl4)
rospy.Subscriber("/platform/distance/fl", Int16, vl5)
rospy.Subscriber("/platform/distance/fr", Int16, vl6)
rospy.Timer(rospy.Duration(1), cb)
rospy.spin()
