import tkinter as tk

BUFFER = 8

class images:   # Image class containing image paths
    wheelchair          = "images/wheelchair.png"          #image_label
    left_up_green       = "images/left up green.png"       #image_label2
    left_middle_green   = "images/left middle green.png"   #image_label3
    left_down_green     = "images/left down green.png"     #image_label4
    right_down_green    = "images/right down green.png"    #image_label5
    right_middle_green  = "images/left middle green.png"   #image_label6
    right_up_green      = "images/right up green.png"      #image_label7
    left_up_yellow      = "images/left up yellow.png"      #image_label8
    left_middle_yellow  = "images/left middle yellow.png"  #image_label9
    left_down_yellow    = "images/left down yellow.png"    #image_label10
    right_down_yellow   = "images/right down yellow.png"   #image_label11
    right_middle_yellow = "images/left middle yellow.png"  #image_label12
    right_up_yellow     = "images/right up yellow.png"     #image_label13
    left_up_red         = "images/left up red.png"         #image_label14
    left_middle_red     = "images/left middle red.png"     #image_label5
    left_down_red       = "images/left down red.png"       #image_label6
    right_down_red      = "images/right down red.png"      #image_label7
    right_middle_red    = "images/left middle red.png"     #image_label18
    right_up_red        = "images/right up red.png"        #image_label19



def close_window():
    root.destroy()

def change_image(image):
    return tk.PhotoImage(file=image)

import time

def change_left_up():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label2.place_forget()
        image_label14.place(relx=0.146, rely=0.4)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label2.place_forget()
        image_label8.place(relx=0.1, rely=0.1)

def change_left_middle():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label3.place_forget()
        image_label15.place(relx=0.1, rely=0.33)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label3.place_forget()
        image_label9.place(relx=0.125, rely=0.33)


def change_left_down():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label4.place_forget()
        image_label16.place(relx=0.11, rely=0.7)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label4.place_forget()
        image_label10.place(relx=0.11, rely=0.7)


def change_right_down():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label5.place_forget()
        image_label17.place(relx=0.42, rely=0.7)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label5.place_forget()
        image_label11.place(relx=0.42, rely=0.7)


def change_right_middle():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label6.place_forget()
        image_label18.place(relx=0.485, rely=0.33)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label6.place_forget()
        image_label12.place(relx=0.485, rely=0.33)


def change_right_up():
    if BUFFER < 5:
     # Hide the green image and show the yellow image
        image_label7.place_forget()
        image_label19.place(relx=0.42, rely=0.1)

    if 5 <= BUFFER <= 10:
     # Hide the green image and show the red image
        image_label7.place_forget()
        image_label13.place(relx=0.42, rely=0.1)


root = tk.Tk()
root.attributes("-fullscreen", True)


# Load the wheeelchair image
photo = tk.PhotoImage(file=images.wheelchair)
# Create a label with the image
image_label = tk.Label(root, image=photo)
image_label.pack(side=tk.LEFT)
image_label.place(relx=0.2, rely=0.2)


# Load left up green image
photo2 = tk.PhotoImage(file=images.left_up_green)
image_label2 = tk.Label(root, image=photo2)
image_label2.pack(side=tk.LEFT)
image_label2.place(relx=0.1, rely=0.1)

# Load left middle green image
photo3 = tk.PhotoImage(file=images.left_middle_green)
image_label3 = tk.Label(root, image=photo3)
image_label3.pack(side=tk.LEFT)
image_label3.place(relx=0.095, rely=0.33)

# Load the left down green image
photo4 = tk.PhotoImage(file=images.left_down_green)
image_label4 = tk.Label(root, image=photo4)
image_label4.pack(side=tk.LEFT)
image_label4.place(relx=0.11, rely=0.7)

# Load the right down green image
photo5 = tk.PhotoImage(file=images.right_down_green)
image_label5 = tk.Label(root, image=photo5)
image_label5.pack(side=tk.LEFT)
image_label5.place(relx=0.42, rely=0.7)

# Load the right middle green image
photo6 = tk.PhotoImage(file=images.left_middle_green)
image_label6 = tk.Label(root, image=photo6)
image_label6.pack(side=tk.LEFT)
image_label6.place(relx=0.485, rely=0.33)

# Load the right up green image
photo7 = tk.PhotoImage(file=images.right_up_green)
image_label7 = tk.Label(root, image=photo7)
image_label7.pack(side=tk.LEFT)
image_label7.place(relx=0.42, rely=0.1)

# Load the left up yellow image
photo8 = tk.PhotoImage(file=images.left_up_yellow)
image_label8 = tk.Label(root, image=photo8)
image_label8.place_forget()

# Load the left middle yellow image
photo9 = tk.PhotoImage(file=images.left_middle_yellow)
image_label9 = tk.Label(root, image=photo9)
image_label9.place_forget()

# Load the left down yellow image
photo10 = tk.PhotoImage(file=images.left_down_yellow)
image_label10 = tk.Label(root, image=photo10)
image_label10.place_forget()

# Load the right down yellow image
photo11 = tk.PhotoImage(file=images.right_down_yellow)
image_label11 = tk.Label(root, image=photo11)
image_label11.place_forget()

# Load the right middle yellow image
photo12 = tk.PhotoImage(file=images.left_middle_yellow)
image_label12 = tk.Label(root, image=photo12)
image_label12.place_forget()

#  Load the right up yellow image
photo13 = tk.PhotoImage(file=images.right_up_yellow)
image_label13 = tk.Label(root, image=photo13)
image_label13.place_forget()

# Load left up red image
photo14 = tk.PhotoImage(file=images.left_up_red)
image_label14 = tk.Label(root, image=photo14)
image_label14.place_forget()

# Load left middle red image
photo15 = tk.PhotoImage(file=images.left_middle_red)
image_label15 = tk.Label(root, image=photo15)
image_label15.place_forget()

# Load left down red image
photo16 = tk.PhotoImage(file=images.left_down_red)
image_label16 = tk.Label(root, image=photo16)
image_label16.place_forget()

# Load right down red image
photo17 = tk.PhotoImage(file=images.right_down_red)
image_label17 = tk.Label(root, image=photo17)
image_label17.place_forget()

# Load right middle red image
photo18 = tk.PhotoImage(file=images.left_middle_red)
image_label18 = tk.Label(root, image=photo18)
image_label18.place_forget()

# Load right up red image
photo19 = tk.PhotoImage(file=images.right_up_red)
image_label19 = tk.Label(root, image=photo19)
image_label19.place_forget()


# Schedule the show_image2() function to run every 1 second
root.after(1000, change_left_up)
root.after(1000, change_left_middle)
root.after(1000, change_left_down)
root.after(1000, change_right_down)
root.after(1000, change_right_middle)
root.after(1000, change_right_up)

# Add a close button
close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 24), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

root.mainloop()
