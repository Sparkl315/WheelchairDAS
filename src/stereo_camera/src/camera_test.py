import numpy as np 
import cv2
 

CAMERA_STARTED = False

def start_capture():
  global CamL, CamR, CAMERA_STARTED
  CamL = cv2.VideoCapture(0)
  CamR = cv2.VideoCapture(2)
  ## For Linux VM
  # CamL= cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw,format=YUY2,\
  #                       width=640,height=480,framerate=30/1 ! videoconvert ! \
  #                       video/x-raw, format=BGR ! appsink drop=1 ", cv2.CAP_GSTREAMER)
  # CamR= cv2.VideoCapture("v4l2src device=/dev/video2 ! video/x-raw,format=YUY2,\
  #                       width=640,height=480,framerate=30/1 ! videoconvert ! \
  #                       video/x-raw, format=BGR ! appsink drop=1 ", cv2.CAP_GSTREAMER)
  CAMERA_STARTED = True

def ShowDisparity(imgL, imgR, bSize = 5):
    # Initialize the stereo block matching object 
    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=bSize)

    # Compute the disparity image
    disparity = stereo.compute(imgL, imgR)

    # Normalize the image for representation
    min = disparity.min()
    max = disparity.max()
    disparity = np.uint8(255 * (disparity - min) / (max - min))
    
    # Plot the result
    return disparity

def fn():
  start_capture()
  
  while CAMERA_STARTED:
  
    # Capturing and storing left and right camera images
    retL, imgL= CamL.read()
    retR, imgR= CamR.read()

    if retL and retR:
      imgL_gray = cv2.cvtColor(imgL,cv2.COLOR_BGR2GRAY)
      imgR_gray = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)

    Combined_image = np.concatenate((imgL, imgR), axis=1)
    Combined_image_gray = np.concatenate((imgL_gray, imgR_gray), axis=1)
    disparity_image = ShowDisparity(imgL = imgL_gray, imgR = imgR_gray, bSize = 5)

    # Displaying the disparity map
    # cv2.imshow("camera_view", Combined_image)
    cv2.imshow("camera_view", disparity_image)

    # Close window using esc key
    if cv2.waitKey(1) == ord('q'):
      break

  else:
    start_capture()

if __name__ == "__main__":
  fn()