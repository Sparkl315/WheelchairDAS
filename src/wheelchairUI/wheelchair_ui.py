import rospy
import tkinter as tk
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class images:   # Image class containing image paths
    wheelchair          = "images/wheelchair.png"

    green_indicator     = ["images/left up green.png",
                            "images/left middle green.png",
                            "images/left down green.png",
                            "images/right down green.png",
                            "images/right middle green.png",
                            "images/right up green.png"]
    
    yellow_indicator    = ["images/left up yellow.png",
                            "images/left middle yellow.png",
                            "images/left down yellow.png",
                            "images/right down yellow.png",
                            "images/right middle yellow.png",
                            "images/right up yellow.png"]
    
    red_indicator       = ["images/left up red.png",
                            "images/left middle red.png",
                            "images/left down red.png",
                            "images/right down red.png",
                            "images/right middle red.png",
                            "images/right up red.png"]


## UI Functions ##
root = tk.Tk()
root.geometry("1024x768")
root.configure(bg="#ffffff") # set background color to white

def close_window():
    root.destroy()

def change_image(image):
    return tk.PhotoImage(file = image)

def update_gui():
    listener()
    root.after(500, update_gui) # call listener after 100 ms

close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 12), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

#Load the wheelchair
wc = tk.PhotoImage(file = images.wheelchair)
wc_label = tk.Label(root, image=wc)
wc_label.pack(side=tk.LEFT)
wc_label.place(relx=0.055, rely=0.08)

indicators = [
    tk.Frame(root, width=30, height=200, bg="#f00"),
    tk.Frame(root, width=30, height=200, bg="#f00"),
    tk.Frame(root, width=30, height=200, bg="#f00"),
    tk.Frame(root, width=30, height=200, bg="#f00"),
    tk.Frame(root, width=30, height=200, bg="#f00"),
    tk.Frame(root, width=30, height=200, bg="#f00")
]

indicators[0].place(x=25, y=150, anchor="w")
indicators[1].place(x=25, y=360., anchor="w")
indicators[2].place(x=25, y=580, anchor="w")
indicators[3].place(x=485, y=580, anchor="w")
indicators[4].place(x=485, y=360, anchor="w")
indicators[5].place(x=485, y=150, anchor="w")

# cam_image_label = tk.Label(root, bg="#cccccc")
# cam_image_label.place(x=384, y=288, anchor="w")

# def convert_to_photoimage(img):
#     # Convert the numpy array to a PhotoImage
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     h, w, d = img.shape
#     img_flat = img.reshape((-1,))
#     img_bytes = b"".join([bytes([x]) for x in img_flat])
#     img_tk = tk.PhotoImage(width=w, height=h, data=img_bytes, format="ppm")
#     return img_tk
## ROS Subscriber Node ##

def callback_obs(data):
    global indicators
    for i, e in enumerate(data.data):
        if (e == 0):
            indicators[i].configure(bg="#0f0")
        elif (e == 1):
            indicators[i].configure(bg="#f00")
        elif (e == 2):
            indicators[i].configure(bg="#f00")

# def callback_cam(msg):
#     bridge = CvBridge()
#     # Convert the ROS image message to a numpy array
#     img = bridge.imgmsg_to_cv2(msg, "bgr8")
#     img_tk = convert_to_photoimage(img)
#     cam_image_label.configure(image=img_tk)
#     cam_image_label.image = img_tk
    

def listener():
    rospy.Subscriber('/sensor/obstacle_state', Int32MultiArray, callback_obs)
    # if root.winfo_exists():
    #     rospy.Subscriber('/sensor/camera', Image, callback_cam)

if __name__ == "__main__":
    ## ROS Subscribe ##
    rospy.init_node('listener', anonymous=True)
    update_gui()
    root.mainloop()
