import tkinter as tk

BUFFER = 100

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

root = tk.Tk()
root.attributes("-fullscreen", True)


# Load the first image
photo = tk.PhotoImage(file=images.wheelchair)

# Create a label with the image
image_label = tk.Label(root, image=photo)
image_label.pack(side=tk.LEFT)
image_label.place(relx=0.2, rely=0.2)

# Load the second image
photo2 = tk.PhotoImage(file=images.left_middle_green)

# Create a label with the image
image_label2 = tk.Label(root, image=photo2)
image_label2.pack(side=tk.LEFT)
image_label2.place(relx=0.146, rely=0.4)

# Load the second image
photo3 = tk.PhotoImage(file=images.right_middle_green)

# Create a label with the image
image_label3 = tk.Label(root, image=photo3)
image_label3.pack(side=tk.LEFT)
image_label3.place(relx=0.425, rely=0.4)


# Add a close button

close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 24), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

root.mainloop()
