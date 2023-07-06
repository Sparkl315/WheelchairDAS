import cv2
import numpy as np

# Set up cameras
left_camera = cv2.VideoCapture('/dev/video0')
right_camera = cv2.VideoCapture('/dev/video2')
left_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
left_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
right_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
right_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# StereoSGBM settings
min_disparity = 0
num_disparities = 16 * 6
block_size = 11
P1 = 8 * 3 * block_size ** 2
P2 = 32 * 3 * block_size ** 2
disp12_max_diff = 1
uniqueness_ratio = 15
speckle_window_size = 100
speckle_range = 32

# Create trackbars for parameter tuning
cv2.namedWindow('StereoSGBM Parameters')
cv2.createTrackbar('Num Disparities', 'StereoSGBM Parameters', num_disparities, 256, lambda x: None)
cv2.createTrackbar('Block Size', 'StereoSGBM Parameters', block_size, 255, lambda x: None)
cv2.createTrackbar('P1', 'StereoSGBM Parameters', P1, 10000, lambda x: None)
cv2.createTrackbar('P2', 'StereoSGBM Parameters', P2, 10000, lambda x: None)
cv2.createTrackbar('Disp12 Max Diff', 'StereoSGBM Parameters', disp12_max_diff, 255, lambda x: None)
cv2.createTrackbar('Uniqueness Ratio', 'StereoSGBM Parameters', uniqueness_ratio, 100, lambda x: None)
cv2.createTrackbar('Speckle Window Size', 'StereoSGBM Parameters', speckle_window_size, 500, lambda x: None)
cv2.createTrackbar('Speckle Range', 'StereoSGBM Parameters', speckle_range, 100, lambda x: None)

while True:
    ret1, left_frame = left_camera.read()
    ret2, right_frame = right_camera.read()

    if not ret1 or not ret2:
        break

    # Get current parameter values from trackbars
    num_disparities = cv2.getTrackbarPos('Num Disparities', 'StereoSGBM Parameters')
    block_size = cv2.getTrackbarPos('Block Size', 'StereoSGBM Parameters')
    P1 = cv2.getTrackbarPos('P1', 'StereoSGBM Parameters')
    P2 = cv2.getTrackbarPos('P2', 'StereoSGBM Parameters')
    disp12_max_diff = cv2.getTrackbarPos('Disp12 Max Diff', 'StereoSGBM Parameters')
    uniqueness_ratio = cv2.getTrackbarPos('Uniqueness Ratio', 'StereoSGBM Parameters')
    speckle_window_size = cv2.getTrackbarPos('Speckle Window Size', 'StereoSGBM Parameters')
    speckle_range = cv2.getTrackbarPos('Speckle Range', 'StereoSGBM Parameters')

    # StereoSGBM settings
    stereoSGBM = cv2.StereoSGBM_create(
        minDisparity=min_disparity,
        numDisparities=num_disparities,
        blockSize=block_size,
        P1=P1,
        P2=P2,
        disp12MaxDiff=disp12_max_diff,
        uniquenessRatio=uniqueness_ratio,
        speckleWindowSize=speckle_window_size,
        speckleRange=speckle_range,
    )

    # Convert to grayscale
    left_gray = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)

    # Compute disparity map
    disparity_map = stereoSGBM.compute(left_gray, right_gray)

    # Normalize the disparity map for display
    norm_disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Show the disparity map
    cv2.imshow('Disparity Map', norm_disparity_map)
  
