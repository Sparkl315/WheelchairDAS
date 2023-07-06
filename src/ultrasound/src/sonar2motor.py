#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

def callback(data):
    log_msgs = [""] * len(data.data)
    for i, val in enumerate(data.data):
        if val <= 0.15:
            log_msgs[i] = "red"
        elif val > 0.15 and val <= 0.4:
            log_msgs[i] = "yellow"
        else:
            log_msgs[i] = "green"

def listener():
    rospy.init_node('ultrasound_listener', anonymous=True)
    rospy.Subscriber("/sensor/ultrasound", Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
