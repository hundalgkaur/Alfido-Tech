import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from PIL import Image, ImageTk

# Function to generate a random password
def generate_password():
    password_length = int(length_var.get())
    password_option = option_var.get()
    
    if password_option == "Weak":
        password_chars = string.ascii_letters
    elif password_option == "Medium":
        password_chars = string.ascii_letters + string.digits
    else:  # Strong
        password_chars = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(password_chars) for _ in range(password_length))
    password_var.set(password)

# Function to regenerate a new random password
def regenerate_password():
    generate_password()

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    password = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x550")  # Increased window size

# Disable window resizing
root.resizable(False, False)

length_var = tk.StringVar()
option_var = tk.StringVar()
password_var = tk.StringVar()

# Set window background image
bg_image = Image.open("H:/cafe/assets/images/to_do_list_PYTHON/back1.png")  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

navbar = tk.Frame(root, bg="blue", height=50)
navbar.pack(fill="x")

title_label = tk.Label(navbar, text="Password Generator", font=("Arial", 20, "bold"), fg="white", bg="blue")
title_label.pack(pady=10)

canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")  # Increased canvas height and added background color
canvas.place(relx=0.5, rely=0.5, anchor="center")  # Center the canvas

# Add padding to the canvas content
content_frame = tk.Frame(canvas, bg="lightgray", padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

option_label = tk.Label(content_frame, text="Strength:", fg="black", font=("Arial", 14))
option_label.pack()

option_combobox = ttk.Combobox(content_frame, values=["weak", "medium", "strong"], textvariable=option_var, font=("Arial", 12))
option_combobox.set("weak")
option_combobox.pack()

# Spacer label to add space between labels
spacer_label = tk.Label(content_frame, text="", bg="lightgray", font=("Arial", 12))
spacer_label.pack()

length_label = tk.Label(content_frame, text="length:", fg="black", font=("Arial", 14))
length_label.pack()

length_entry = ttk.Entry(content_frame, textvariable=length_var, font=("Arial", 12))
length_entry.pack()

generate_button = tk.Button(
    content_frame, 
    text="Generate Password", 
    command=generate_password, 
    bg="green", 
    width=15, 
    height=1,
    fg="white",
    font=("Verdana", 13, "bold"),
    anchor="center"
)
generate_button.pack(pady=10)

password_label = tk.Label(content_frame, text="Generated Password:", font=("Arial", 14))
password_label.pack()

password_display = tk.Entry(content_frame, textvariable=password_var, state="readonly", width=20, font=("Arial", 12))
password_display.pack()

button_frame = tk.Frame(content_frame, bg="lightgray", pady=10)  # Added padding between buttons
button_frame.pack()

copy_button = tk.Button(
    button_frame, 
    text="Copy ", 
    command=copy_to_clipboard, 
    bg="blue", 
    width=10, 
    height=1,
    fg="white",
    font=("Verdana", 13, "bold"),
    anchor="center" 
)
copy_button.pack(side="left", padx=10)  # Added space between buttons

regenerate_button = tk.Button(
    button_frame, 
    text="Regenerate", 
    command=regenerate_password, 
    bg="blue", 
    width=10, 
    height=1,
    fg="white",
    font=("Verdana", 13, "bold"),
    anchor="center"
)
regenerate_button.pack(side="left")

# Set a style for green buttons with white text and bold
style = ttk.Style()
style.configure("Green.TButton", background="green", foreground="white", font=("Arial", 12, "bold"))

root.mainloop()
