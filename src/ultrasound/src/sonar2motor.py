#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

AUTO_TUNE_AVAILABLE = True
Obstacle_Exists = [0, 0, 0, 0 ,0 ,0]    // 0 : Clear , 1 : Obstacle Exists   // Need Auto Tuning
Output_State    = [0, 0, 0, 0, 0, 0]    // 0 : Safe  , 1 : Obstacle Detected , 2 : Obstacle Near

def callback(data):
    log_msgs = [""] * len(data.data)
    for i, val in enumerate(data.data):
        if val <= 0.15 and val != 0:
            if (AUTO_TUNE_AVAILABLE): Obstacle_exists[i] = 1
            else: Obstacle_exists[i] = 0
            Output_State[i] = 2
        elif val > 0.15 and val <= 0.4:
            Obstacle_exists[i] = 0
            Output_State[i] = 1
        else:
            Obstacle_exists[i] = 0
            Output_State[i] = 0

def listener():
    rospy.init_node('ultrasound_listener', anonymous=True)
    rospy.Subscriber("/sensor/ultrasound", Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
