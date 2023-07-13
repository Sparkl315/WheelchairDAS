import cv2
import numpy as np
import yaml

BS_prev = None  # Block Size
ND_prev = None  # Num Disparity

IMAGE_SIZE = (640, 480)

## camera yaml file ##
camL_calib = "cameraL.yaml"
camR_calib = "cameraR.yaml"

def set_camera_resolution(cam, w, h):
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

def image_rectify(imgL, imgR, calibL, calibR):
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

    return [imgL_rect, imgR_rect]

## main ##
if __name__ == "__main__":
    # Set up cameras
    left_camera = cv2.VideoCapture('/dev/video0')
    right_camera = cv2.VideoCapture('/dev/video2')

    set_camera_resolution(left_camera, IMAGE_SIZE[0], IMAGE_SIZE[1])
    set_camera_resolution(right_camera, IMAGE_SIZE[0], IMAGE_SIZE[1])

    # Create trackbars for parameter tuning
    cv2.namedWindow('StereoBM Parameters')
    cv2.createTrackbar('Num Disparities', 'StereoBM Parameters', 16, 256, lambda x: None)
    cv2.createTrackbar('Block Size', 'StereoBM Parameters', 15, 255, lambda x: None)
    cv2.createTrackbar('Pre-filter Cap', 'StereoBM Parameters', 31, 63, lambda x: None)
    cv2.createTrackbar('Texture Threshold', 'StereoBM Parameters', 0, 255, lambda x: None)


    while True:
        ret1, left_frame = left_camera.read()
        ret2, right_frame = right_camera.read()

        if not ret1 or not ret2:
            break
        
        left_frame, right_frame = image_rectify(left_frame, right_frame, camL_calib, camR_calib)
        # Get current parameter values from trackbars
        num_disparities = cv2.getTrackbarPos('Num Disparities', 'StereoBM Parameters')
        block_size = cv2.getTrackbarPos('Block Size', 'StereoBM Parameters')
        texture_thres = cv2.getTrackbarPos('Texture Threshold', 'StereoBM Parameters')

        # StereoBM settings
        # Check Variable Validity
        if (num_disparities % 16 != 0):
            num_disparities = ND_prev
        else:
            if (num_disparities != ND_prev):
                print("BlockSize set to ", num_disparities)
            ND_prev = num_disparities

        if (block_size % 2 == 0 or block_size < 5):
            block_size = BS_prev
        else:
            if (block_size != BS_prev):
                print("BlockSize set to ", block_size)
            BS_prev = block_size
            
        stereoBM = cv2.StereoBM_create(num_disparities, block_size)
        stereoBM.setTextureThreshold(texture_thres)
        # Convert to grayscale
        left_gray = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
        right_gray = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)

        # Compute disparity map
        disparity_map = stereoBM.compute(left_gray, right_gray)
       
        # # Normalize the disparity map for display
        edge_disparity_map = cv2.normalize(disparity_map, None, alpha=-16, beta=240, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

        # # Convert to color map
        edge_disparity_color_map = cv2.applyColorMap(edge_disparity_map, cv2.COLORMAP_JET)

        focal_length = 235  # Camera focal length (mm)
        depth_map = np.zeros_like(disparity_map, dtype=np.float32)
        for y in range(depth_map.shape[0]):
            for x in range(depth_map.shape[1]):
                if edge_disparity_map[y, x] > 0:
                    if disparity_map[y, x] != 0:
                        depth_map[y, x] = focal_length / disparity_map[y, x]
                    else:
                        depth_map[y, x] = 0
        print(np.min(disparity_map), np.max(disparity_map))
        edge_depth_map = cv2.normalize(depth_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        # Show the disparity map
        cv2.imshow('Image', left_gray)
        cv2.imshow('Disparity Map', edge_disparity_color_map)
        # cv2.imshow('Depth Map', depth_map)

        # Check for keypress to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    left_camera.release()
    right_camera.release()
    cv2.destroyAllWindows()
