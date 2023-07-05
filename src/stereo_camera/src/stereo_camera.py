import numpy as np 
import cv2

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
        self.CAMERA_STARTED = True

    def camera_read(self):
        retL, self.imgL_color = self.Cam_L.read()
        retR, self.imgR_color = self.Cam_R.read()

        if retL and retR:   # Cam_L and Cam_R available
            self.imgL_gray = cv2.cvtColor(self.imgL_color,cv2.COLOR_BGR2GRAY)
            self.imgR_gray = cv2.cvtColor(self.imgR_color,cv2.COLOR_BGR2GRAY)

    def show_image(self, image):
        cv2.imshow("image", image)

if __name__ == "__main__":
    stereo_cam = stereo_camera
    while (stereo_cam.CAMERA_STARTED):
        stereo_cam.camera_read()
        stereo_cam.show_image(stereo_cam.imgL_color)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        stereo_cam.start_capture(CamLID = 0, CamRID = 2)
    