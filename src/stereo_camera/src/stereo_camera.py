#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np 
import cv2

class image2ros:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('camera_publisher', anonymous=True)
    
        # Initialize the publisher to publish images to the "/sensor/camera" topic
        self.image_pub = rospy.Publisher("/sensor/camera", Image, queue_size=10)
    
        # Create a CvBridge object to convert between OpenCV images and ROS images
        bridge = CvBridge()

    def publish_image(self, image):
        # Convert the OpenCV image to a ROS image message
        ros_image = bridge.cv2_to_imgmsg(image, "bgr8")

        # Publish the ROS image message to the "/sensor/camera" topic
        image_pub.publish(ros_image)
    
class stereo_camera:
    CAMERA_STARTED = False
    imgL_color = None
    imgR_color = None
    imgL_gray  = None
    imgR_gray  = None

    def start_capture(self, CamLID = 0, CamRID = 2):
        # Start Camera
        self.Cam_L = cv2.VideoCapture(CamLID)
        self.Cam_R = cv2.VideoCapture(CamRID)
        ## For Linux VM
        # CamL= cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,\
        #                       width=640,height=480,framerate=30/1 ! videoconvert ! \
        #                       video/x-raw, format=BGR ! appsink drop=1 ", cv2.CAP_GSTREAMER)
        # CamR= cv2.VideoCapture("v4l2src device=/dev/video2 ! video/x-raw,format=YUY2,\
        #                       width=640,height=480,framerate=30/1 ! videoconvert ! \
        #                       video/x-raw, format=BGR ! appsink drop=1 ", cv2.CAP_GSTREAMER)
        
        # Set Resolution
        self.set_resolution(self.Cam_L)
        self.set_resolution(self.Cam_R)
        
        self.CAMERA_STARTED = True

    def camera_read(self):
        retL, self.imgL_color = self.Cam_L.read()
        retR, self.imgR_color = self.Cam_R.read()

        if retL and retR:   # Cam_L and Cam_R available
            self.imgL_gray = cv2.cvtColor(self.imgL_color,cv2.COLOR_BGR2GRAY)
            self.imgR_gray = cv2.cvtColor(self.imgR_color,cv2.COLOR_BGR2GRAY)
            return True
        else:
            return False

    def set_resolution(self, Cam, res_w = 640, res_h = 480):
        Cam.set(cv2.CAP_PROP_FRAME_WIDTH, res_w)
        Cam.set(cv2.CAP_PROP_FRAME_HEIGHT, res_h)
        
    def show_image(self, name, image):
        cv2.imshow(name, image)

if __name__ == "__main__":
    img2ros = image2ros()
    stereo_cam = stereo_camera()
    stereo_cam.start_capture(CamLID = 0, CamRID = 2)
    while (stereo_cam.CAMERA_STARTED):
        if (stereo_cam.camera_read()):
            if not (rospy.is_shutdown()):
                img2ros.publish_image(stereo_cam.imgL_color)
            else:
                print("ROS Not Started, No Image Sent.")
        # stereo_cam.show_image("imgL", stereo_cam.imgL_color)
        # stereo_cam.show_image("imgR", stereo_cam.imgR_color)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        stereo_cam.start_capture(CamLID = 0, CamRID = 2)
