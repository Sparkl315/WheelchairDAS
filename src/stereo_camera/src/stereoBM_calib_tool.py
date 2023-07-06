import cv2
import numpy as np

# Set up cameras
left_camera = cv2.VideoCapture('/dev/video0')
right_camera = cv2.VideoCapture('/dev/video2')
left_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
left_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
right_camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
right_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create trackbars for parameter tuning
cv2.namedWindow('StereoBM Parameters')
cv2.createTrackbar('Num Disparities', 'StereoBM Parameters', 16, 256, lambda x: None)
cv2.createTrackbar('Block Size', 'StereoBM Parameters', 15, 255, lambda x: None)

while True:
    ret1, left_frame = left_camera.read()
    ret2, right_frame = right_camera.read()

    if not ret1 or not ret2:
        break

    # Get current parameter values from trackbars
    num_disparities = cv2.getTrackbarPos('Num Disparities', 'StereoBM Parameters')
    block_size = cv2.getTrackbarPos('Block Size', 'StereoBM Parameters')

    # StereoBM settings
    stereoBM = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)

    # Convert to grayscale
    left_gray = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)

    # Compute disparity map
    disparity_map = stereoBM.compute(left_gray, right_gray)

    # Normalize the disparity map for display
    norm_disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Show the disparity map
    cv2.imshow('Disparity Map', norm_disparity_map)

    # Check for keypress to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

left_camera.release()
right_camera.release()
cv2.destroyAllWindows()
