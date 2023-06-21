import tkinter as tk

BUFFER = 100

def close_window():
    root.destroy()

root = tk.Tk()
root.attributes("-fullscreen", True)


# Load the first image
image_path = "wheelchair.png"  # Replace with the actual path to your image
photo = tk.PhotoImage(file=image_path)

# Create a label with the image
image_label = tk.Label(root, image=photo)
image_label.pack(side=tk.LEFT)
image_label.place(relx=0.2, rely=0.2)

# Load the second image
image_path2 = "left middle green.png"  # Replace with the actual path to your image
photo2 = tk.PhotoImage(file=image_path2)

# Create a label with the image
image_label2 = tk.Label(root, image=photo2)
image_label2.pack(side=tk.LEFT)
image_label2.place(relx=0.146, rely=0.4)

# Load the second image
image_path3 = "right middle green.png"  # Replace with the actual path to your image
photo3 = tk.PhotoImage(file=image_path3)

# Create a label with the image
image_label3 = tk.Label(root, image=photo3)
image_label3.pack(side=tk.LEFT)
image_label3.place(relx=0.425, rely=0.4)


# Add a close button

close_button = tk.Button(root, text="X", command= close_window, font=("Arial", 24), padx=10, pady=5)
close_button.pack(side= tk.TOP, anchor=tk.NE)

root.mainloop()