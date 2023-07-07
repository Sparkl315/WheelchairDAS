import tkinter as tk
from PIL import Image, ImageTk
BUFFER = BUFFER2 = BUFFER3 = BUFFER4 = BUFFER5 = BUFFER6 = 2

class images:   # Image class containing image paths
    wheelchair          = "images/wheelchair.png"          #image_label
    left_up_green       = "images/left up green.png"       #image_label2
    left_middle_green   = "images/left middle green.png"   #image_label3
    left_down_green     = "images/left down green.png"     #image_label4
    right_down_green    = "images/right down green.png"    #image_label5
    right_middle_green  = "images/right middle green.png"  #image_label6
    right_up_green      = "images/right up green.png"      #image_label7
    left_up_yellow      = "images/left up yellow.png"      #image_label8
    left_middle_yellow  = "images/left middle yellow.png"  #image_label9
    left_down_yellow    = "images/left down yellow.png"    #image_label10
    right_down_yellow   = "images/right down yellow.png"   #image_label11
    right_middle_yellow = "images/right middle yellow.png"  #image_label12
    right_up_yellow     = "images/right up yellow.png"     #image_label13
    left_up_red         = "images/left up red.png"         #image_label14
    left_middle_red     = "images/left middle red.png"     #image_label5
    left_down_red       = "images/left down red.png"       #image_label6
    right_down_red      = "images/right down red.png"      #image_label7
    right_middle_red    = "images/right middle red.png"     #image_label18
    right_up_red        = "images/right up red.png"        #image_label19
    rear_mirror         = "images/rear mirror.jpg"         #rear mirror



def close_window():
    root.destroy()

def change_image(image):
    return ImageTk.PhotoImage(image)


import time

def change_left_up():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label2.place_forget()
        image_label14.place(relx=0.12, rely=0.1)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label2.place_forget()
        image_label8.place(relx=0.11, rely=0.10)

def change_left_middle():
    if BUFFER2 < 5:
     # Hide the green image and show the yellow image
        image_label3.place_forget()
        image_label15.place(relx=0.108, rely=0.26)

    if 5 <= BUFFER2 <= 10:
     # Hide the green image and show the red image
        image_label3.place_forget()
        image_label9.place(relx=0.10, rely=0.26)


def change_left_down():
    if BUFFER3 < 5:
     # Hide the green image and show the yellow image
        image_label4.place_forget()
        image_label16.place(relx=0.12, rely=0.52)

    if 5 <= BUFFER3 <= 10:
     # Hide the green image and show the red image
        image_label4.place_forget()
        image_label10.place(relx=0.11, rely=0.52)


def change_right_down():
    if BUFFER4 < 5:
     # Hide the green image and show the yellow image
        image_label5.place_forget()
        image_label17.place(relx=0.43, rely=0.52)

    if 5 <= BUFFER4 <= 10:
     # Hide the green image and show the red image
        image_label5.place_forget()
        image_label11.place(relx=0.43, rely=0.52)


def change_right_middle():
    if BUFFER5 < 5:
     # Hide the green image and show the yellow image
        image_label6.place_forget()
        image_label18.place(relx=0.44, rely=0.25)

    if 5 <= BUFFER5 <= 10:
     # Hide the green image and show the red image
        image_label6.place_forget()
        image_label12.place(relx=0.44, rely=0.26)

def change_right_up():
    if BUFFER6 < 5:
     # Hide the green image and show the yellow image
        image_label7.place_forget()
        image_label19.place(relx=0.425, rely=0.10)

    if 5 <= BUFFER6 <= 10:
     # Hide the green image and show the red image
        image_label7.place_forget()
        image_label13.place(relx=0.43, rely=0.10)


root = tk.Tk()
root.geometry("1024x768")
# set background color to white
root.configure(bg="#ffffff") 


#Load left up green image
photo2 = Image.open( "images/left up green.png" )
resized2 = photo2.resize ((80, 80), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(resized2)
image_label2 = tk.Label(root, image=photo2)
image_label2.pack(side=tk.LEFT)
image_label2.place(relx=0.1, rely=0.08)

#Load left middle green image
photo3 = Image.open("images/left middle green.png" )
resized3 = photo3.resize ((80, 150), Image.LANCZOS)
photo3 = ImageTk.PhotoImage(resized3)
image_label3 = tk.Label(root, image=photo3)
image_label3.pack(side=tk.LEFT)
image_label3.place(relx=0.09, rely=0.26)

# Load the left down green image
photo4 = Image.open("images/left down green.png" )
resized4 = photo4.resize ((80, 80), Image.LANCZOS)
photo4 = ImageTk.PhotoImage(resized4)
image_label4 = tk.Label(root, image=photo4)
image_label4.pack(side=tk.LEFT)
image_label4.place(relx=0.1, rely=0.55)

# Load the right down green image
photo5 = Image.open("images/right down green.png" )
resized5 = photo5.resize ((80, 80), Image.LANCZOS)
photo5 = ImageTk.PhotoImage(resized5)
image_label5 = tk.Label(root, image=photo5)
image_label5.pack(side=tk.LEFT)
image_label5.place(relx=0.44, rely=0.55)

# Load the right middle green image
photo6 = Image.open("images/right middle green.png")
resized6 = photo6.resize ((80, 150), Image.LANCZOS)
photo6 = ImageTk.PhotoImage(resized6)
image_label6 = tk.Label(root, image=photo6)
image_label6.pack(side=tk.LEFT)
image_label6.place(relx=0.45, rely=0.26)

# Load the right up green image
photo7 = Image.open( "images/right up green.png")
resized7 = photo7.resize ((80, 80), Image.LANCZOS)
photo7 = ImageTk.PhotoImage(resized7)
image_label7 = tk.Label(root, image=photo7)
image_label7.pack(side=tk.LEFT)
image_label7.place(relx=0.437, rely=0.08)


# Load the left up yellow image
photo8 = Image.open(  "images/left up yellow.png")
resized8 = photo8.resize ((80, 80), Image.LANCZOS)
photo8 = ImageTk.PhotoImage(resized8)
image_label8 = tk.Label(root, image=photo8)
image_label8.place_forget()

# Load the left middle yellow image
photo9 = Image.open(  "images/left middle yellow.png")
resized9 = photo9.resize ((80, 150), Image.LANCZOS)
photo9 = ImageTk.PhotoImage(resized9)
image_label9 = tk.Label(root, image=photo9)
image_label9.place_forget()

# Load the left down yellow image
photo10 = Image.open( "images/left down yellow.png")
resized10 = photo10.resize ((80, 80), Image.LANCZOS)
photo10 = ImageTk.PhotoImage(resized10)
image_label10 = tk.Label(root, image=photo10)
image_label10.place_forget()

# Load the right down yellow image
photo11 = Image.open( "images/right down yellow.png")
resized11 = photo11.resize ((80, 80), Image.LANCZOS)
photo11 = ImageTk.PhotoImage(resized11)
image_label11 = tk.Label(root, image=photo11)
image_label11.place_forget()

# Load the right middle yellow image
photo12 = Image.open( "images/right middle yellow.png")
resized12 = photo12.resize ((80, 150), Image.LANCZOS)
photo12 = ImageTk.PhotoImage(resized12)
image_label12 = tk. Label(root, image=photo12)
image_label12.place_forget()

#  Load the right up yellow image
photo13 = Image.open( "images/right up yellow.png")
resized13 = photo13.resize ((80, 80), Image.LANCZOS)
photo13 = ImageTk.PhotoImage(resized13)
image_label13 = tk.Label(root, image=photo13)
image_label13.place_forget()

#////////////////////////////////////////////////////////////////////////////////
#Load the wheelchair
photo = Image.open("images/wheelchair.png")
resized = photo.resize ((250, 250), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized)
image_label = tk. Label(root, image=photo)
image_label.pack(side=tk.LEFT)
image_label.place(relx=0.18, rely=0.2)
#////////////////////////////////////////////////////////////////////////////////

# Load left up red image
photo14 = Image.open("images/left up red.png")
resized14 = photo14.resize ((80, 80), Image.LANCZOS)
photo14 = ImageTk.PhotoImage(resized14)
image_label14 = tk.Label(root, image=photo14)
image_label14.place_forget()

# Load left middle red image
photo15 = Image.open("images/left middle red.png")
resized15 = photo15.resize ((80, 150), Image.LANCZOS)
photo15 = ImageTk.PhotoImage(resized15)
image_label15 = tk.Label(root, image=photo15)
image_label15.place_forget()

# Load left down red image
photo16 = Image.open("images/left down red.png")
resized16 = photo16.resize ((80, 80), Image.LANCZOS)
photo16 = ImageTk.PhotoImage(resized16)
image_label16 = tk.Label(root, image=photo16)
image_label16.place_forget()

#Load right down red image
photo17 = Image.open("images/right down red.png")
resized17 = photo17.resize ((80, 80), Image.LANCZOS)
photo17 = ImageTk.PhotoImage(resized17)
image_label17 = tk.Label(root, image=photo17)
image_label17.place_forget()

#Load right middle red image
photo18 = Image.open("images/right middle red.png")
resized18 = photo18.resize ((80, 150), Image.LANCZOS)
photo18 = ImageTk.PhotoImage(resized18)
image_label18 = tk.Label(root, image=photo18)
image_label18.place_forget()

#Load right up red image
photo19 = Image.open("images/right up red.png")
resized19 = photo19.resize ((80, 80), Image.LANCZOS)
photo19 = ImageTk.PhotoImage(resized19)
image_label19 = tk.Label(root, image=photo19)
image_label19.place_forget()

#Load the rear mirror
photo20 = Image.open("images/rear mirror.jpg")
resized20 = photo20.resize ((250, 250), Image.LANCZOS)
photo20 = ImageTk.PhotoImage(resized20)
image_label20 = tk. Label(root, image=photo20)
image_label20.pack(side=tk.LEFT)
image_label20.place(relx=0.6, rely=0.5)


# Schedule the show_image2() function to run every 1 second
root.after(1000, change_left_up)
root.after(1000, change_left_middle)
root.after(1000, change_left_down)
root.after(1000, change_right_down)
root.after(1000, change_right_middle)
root.after(1000, change_right_up)

# Add a close button
close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 12), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

if __name__ == "__main__":
    root.mainloop()
