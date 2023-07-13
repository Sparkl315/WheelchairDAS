#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import Float64MultiArray, Int32MultiArray

# Start Serial Port Connection
ser = serial.Serial('/dev/ttyUSB1', 115200)

AUTO_TUNE_AVAILABLE = True
Obstacle_Exists = [0, 0, 0, 0 ,0 ,0]    # 0 : Clear , 1 : Obstacle Exists   # Need Auto Tuning
Output_State    = [0, 0, 0, 0, 0, 0]    # 0 : Safe  , 1 : Obstacle Detected , 2 : Obstacle Near

def callback(data):
    log_msgs = [""] * len(data.data)
    for i, val in enumerate(data.data):
        if val <= 0.15 and val != 0:
            if (AUTO_TUNE_AVAILABLE): Obstacle_Exists[i] = 1
            else: Obstacle_Exists[i] = 0
            Output_State[i] = 2
        elif val > 0.15 and val <= 0.4:
            Obstacle_Exists[i] = 1
            Output_State[i] = 1
        else:
            Obstacle_Exists[i] = 0
            Output_State[i] = 0
            
    OE_String = "".join(str(x) for x in Obstacle_Exists)
    ser.write(OE_String.encode())
    # print(OE_String.encode())

    
    state_msg = Int32MultiArray(data=Output_State)
    state_pub.publish(state_msg)

def listener():
    global state_pub
    rospy.init_node('ultrasound_listener', anonymous=True)
    state_pub = rospy.Publisher('/sensor/obstacle_state', Int32MultiArray, queue_size=10)
    rospy.Subscriber("/sensor/ultrasound", Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
