import tkinter as tk

BUFFER = 1

class images:   # Image class containing image paths
    wheelchair          = "images/wheelchair.png"
    left_middle_red     = "images/left middle red.png"
    left_middle_green   = "images/left middle green.png"
    right_middle_red    = "images/right middle red.png"
    right_middle_green  = "images/right middle green.png"


def close_window():
    root.destroy()

def change_image(image):
    return tk.PhotoImage(file=image)

import time

def show_image3():
    if BUFFER < 10:
        # Hide the first image and show the second image
        image_label2.configure(image=None)
        image_label3.place(relx=0.146, rely=0.4)

def show_image5():
    if BUFFER < 10:
        # Hide the first image and show the second image
        image_label4.configure(image=None)
        image_label5.place(relx=0.425, rely=0.4)

root = tk.Tk()
root.attributes("-fullscreen", True)


# Load the wheeelchair image
photo = tk.PhotoImage(file=images.wheelchair)

# Create a label with the image
image_label = tk.Label(root, image=photo)
image_label.pack(side=tk.LEFT)
image_label.place(relx=0.2, rely=0.2)


# Load left middle green image
photo2 = tk.PhotoImage(file=images.left_middle_green)

# Create a label with the image
image_label2 = tk.Label(root, image=photo2)
image_label2.pack(side=tk.LEFT)
image_label2.place(relx=0.146, rely=0.4)


# Load left middle red image
photo3 = tk.PhotoImage(file=images.left_middle_red)

# Create a label with the image
image_label3 = tk.Label(root, image=photo3)
image_label3.place_forget()

# Load the right middle green image
photo4 = tk.PhotoImage(file=images.right_middle_green)

# Create a label with the image
image_label4 = tk.Label(root, image=photo4)
image_label4.pack(side=tk.LEFT)
image_label4.place(relx=0.425, rely=0.4)

# Load left middle red image
photo5 = tk.PhotoImage(file=images.right_middle_red)

# Create a label with the image
image_label5 = tk.Label(root, image=photo5)
image_label5.place_forget()

# Schedule the show_image2() function to run every 1 second
root.after(1000, show_image3)
root.after(2000, show_image5)

# Add a close button
close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 24), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

root.mainloop()
