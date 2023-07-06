import numpy as np 
import cv2
import yaml
 
IMAGE_SIZE = (640, 480)
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

def ShowDisparity(imgL, imgR, calibL, calibR):
    # Load calibration data from YAML files
    with open(calibL, 'r') as f:
        calib_data1 = yaml.load(f)
    with open(calibR, 'r') as f:
        calib_data2 = yaml.load(f)

    cameraMatrix1 = np.array(calib_data1['camera_matrix']['data']).reshape(3, 3)
    distCoeffs1 = np.array(calib_data1['distortion_coefficients']['data'])
    cameraMatrix2 = np.array(calib_data2['camera_matrix']['data']).reshape(3, 3)
    distCoeffs2 = np.array(calib_data2['distortion_coefficients']['data'])
    R = np.array(calib_data2['rectification_matrix']['data']).reshape(3, 3)
    P1 = np.array(calib_data1['projection_matrix']['data']).reshape(3, 4)
    P2 = np.array(calib_data2['projection_matrix']['data']).reshape(3, 4)

    # Extract rotation matrix and translation vector from projection matrices
    R1, R2, T = cv2.decomposeProjectionMatrix(P2)[:3]
    R = R2.dot(R1.T)
    t = T[:3].flatten()

    imgL_rect = cv2.undistort(imgL, cameraMatrix1, distCoeffs1)
    imgR_rect = cv2.undistort(imgR, cameraMatrix2, distCoeffs2)
    R1, R2, P1, P2, Q, roi1, roi2 = cv2.stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, IMAGE_SIZE, R, t)

    map1x, map1y = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, P1, IMAGE_SIZE, cv2.CV_32FC1)
    map2x, map2y = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, P2, IMAGE_SIZE, cv2.CV_32FC1)
    imgL_rect = cv2.remap(imgL_rect, map1x, map1y, cv2.INTER_LINEAR)
    imgR_rect = cv2.remap(imgR_rect, map2x, map2y, cv2.INTER_LINEAR)

    # Convert to grayscale
    grayL = cv2.cvtColor(imgL_rect, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR_rect, cv2.COLOR_BGR2GRAY)

    # Initialize the stereo block matching object
    stereo = cv2.StereoBM_create(numDisparities=64, blockSize=25)

    # Compute the disparity image
    disparity = stereo.compute(grayL, grayR)

    # Normalize and scale the image for representation
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
    disparity_image = ShowDisparity(imgL = imgL, imgR = imgR, calibL = "cameraL.yaml", calibR = "cameraR.yaml")

    # Displaying the disparity map
    cv2.imshow("camera_view", Combined_image)
    cv2.imshow("disparity", disparity_image)

    # Close window using esc key
    if cv2.waitKey(1) == ord('q'):
      break

  else:
    start_capture()

if __name__ == "__main__":
  fn()