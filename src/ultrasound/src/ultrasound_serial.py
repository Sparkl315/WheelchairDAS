#!/usr/bin/env python3
import rospy
import serial
from std_msgs.msg import Float64MultiArray

PORT_ADDR   = "/dev/ttyUSB0"
TOTAL_SONAR = 6


class sonar2ros:
    def ros_setup(self):
        rospy.init_node('sonar_pub', anonymous=True)
        self.pub = rospy.Publisher('sensor/ultrasound', Float64MultiArray, queue_size=10)
        rate = rospy.Rate(10) # 10hz
    
    def publish(self, data_array):
        data = Float64MultiArray(data = data_array)
        self.pub.publish(data)


class sonar:
    def port_setup(self, addr = PORT_ADDR):
        self.sonar_data = [0 for i in range(TOTAL_SONAR)]
        self.ser = serial.Serial(addr, baudrate=115200)  # open serial port
        # print(self.ser.name)         # check which port was really used

    def port_close(self):
        self.ser.close()

    def read_data(self):
        try:
            data = self.ser.readline().decode('utf-8')    # reading bytes from serial port
            self.data_proc(str(data))
        except Exception as e:
            print("[read_data()] %s:%s"%(e, data))

    def data_proc(self, inp_data:str):
        data = inp_data.strip("\n").split(" ")
        try:
            for i, e in enumerate(data):
                if (e != ""):
                    self.sonar_data[i] = float(e)
        except IndexError:
            print("Data length doesn't match with designated length: %s"%(inp_data))

if __name__ == "__main__":
    s = sonar()
    s2r = sonar2ros()
    # === main ===
    s.port_setup()
    s2r.ros_setup()
    print("start")
    while not rospy.is_shutdown():
        try:
            s.read_data()
            # print(s.sonar_data)
            s2r.publish(s.sonar_data)
        except Exception as e:
            print(e)
            s.port_close()             # close port
            break
