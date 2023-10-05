
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random

def clear_all_tasks():
    if len(tasks) == 0:
        messagebox.showinfo("Info", "There are no tasks to delete.")
    else:
        confirm = messagebox.askokcancel("Confirm Deletion", "Are you sure you want to delete all tasks?")
        if confirm:
            for task_container in task_items_frame.winfo_children():
                task_container.destroy()
            tasks.clear()
            task_items_frame.update_idletasks()
            task_list_canvas.config(scrollregion=task_list_canvas.bbox("all"))
        else:
            messagebox.showinfo("Info", "No tasks were deleted.")

def add_task():
    task = task_entry.get().strip()  # Remove leading/trailing whitespace
    if task:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        random_color = random.choice(color_shades)

        task_container = tk.Frame(task_items_frame, bg=random_color)
        task_container.grid(sticky="nsew")
        task_container.columnconfigure(1, weight=1)

        check_var = tk.BooleanVar()
        check_button = tk.Checkbutton(task_container, variable=check_var, bg=random_color)
        check_button.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        task_label_text = f"{task} (date: {timestamp})"

        task_label = tk.Label(task_container, text=task_label_text, font=("Arial", 12, "bold"), fg="white", bg=random_color)
        task_label.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="w")

        def delete_task():
            confirm = messagebox.askokcancel("Confirm Deletion", "Are you sure to delete this task?")
            if confirm:
                task_container.destroy()
                tasks.remove((task_label_text, timestamp))
                task_items_frame.update_idletasks()
                task_list_canvas.config(scrollregion=task_list_canvas.bbox("all"))

        delete_icon = Image.open("H:/cafe/assets/images/to_do_list_PYTHON/delete.png")
        delete_icon = delete_icon.resize((20, 20), Image.LANCZOS)
        delete_icon = ImageTk.PhotoImage(delete_icon)

        delete_icon_label = tk.Label(task_container, image=delete_icon, bg=random_color, cursor="hand2")
        delete_icon_label.image = delete_icon
        delete_icon_label.grid(row=0, column=2, padx=(5, 10), pady=5, sticky="e")
        delete_icon_label.bind("<Button-1>", lambda event, container=task_container: delete_task())

        tasks.append((task_label_text, timestamp))
        task_entry.delete(0, tk.END)

        task_items_frame.update_idletasks()
        task_list_canvas.config(scrollregion=task_list_canvas.bbox("all"))
    else:
        messagebox.showwarning("Warning", "Please enter Task name.")

def update_vertical_scrollbar(event):
    canvas_height = task_list_canvas.winfo_height()
    task_items_frame_height = task_items_frame.winfo_reqheight()

    if canvas_height >= task_items_frame_height:
        vertical_scrollbar.grid_forget()
    else:
        vertical_scrollbar.grid(row=5, column=2, rowspan=2, sticky="ns")
        task_list_canvas.configure(yscrollcommand=vertical_scrollbar.set)

root = tk.Tk()
root.title("To Do List App")

window_width = 725
window_height = 600
root.geometry(f"{window_width}x{window_height}")
root.maxsize(window_width, window_height)

# Load and resize the background image
background_image = Image.open("H:/cafe/assets/images/to_do_list_PYTHON/back.png")
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)

#  label for the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

navbar_bg = "navy"
title_fg = "white"
title_font = ("Verdana", 20, "bold")
navbar_height = 100
border_radius = 15

navbar = tk.Canvas(root, bg=navbar_bg, height=navbar_height, borderwidth=0, relief="solid")
navbar.create_polygon(
    0, navbar_height,
    root.winfo_width(), navbar_height,
    root.winfo_width(), 0,
    0, 0,
    outline=navbar_bg,
    fill=navbar_bg
)
navbar.grid(row=0, rowspan=2, column=0, columnspan=2, sticky="ew")

left_icon = Image.open("H:/Note_App/assets/splash_screen.png")
left_icon = left_icon.resize((50, 50), Image.LANCZOS)
left_icon = ImageTk.PhotoImage(left_icon)

left_icon_label = tk.Label(navbar, image=left_icon, bg=navbar_bg)
left_icon_label.image = left_icon
left_icon_label.grid(row=0, column=0, padx=20)


title_label = tk.Label(navbar, text=" ALL TASK's ", font=("Snap ITC", 15, "bold"), fg="white",bg=navbar_bg,height=2)
title_label.grid(row=0, column=1, padx=180)
#----------------
rigth_icon = Image.open("H:/Note_App/assets/splash_screen.png")
rigth_icon = rigth_icon.resize((50, 50), Image.LANCZOS)
rigth_icon = ImageTk.PhotoImage(rigth_icon)

rigth_icon_label = tk.Label(navbar, image=rigth_icon, bg=navbar_bg)
rigth_icon_label.image = rigth_icon
rigth_icon_label.grid(row=0, column=2, padx=20)
#---------------

title_label = tk.Label(text=".....All Task List.....", font=("Ravie", 15, "bold"), fg="black",bg="yellow" , height=1)
title_label.grid(row=4, column=1, padx=80)

left_paned_window = tk.PanedWindow(root, bg="light gray", sashwidth=5, sashrelief="ridge", orient="vertical")
left_paned_window.grid(row=5, column=0, padx=10, pady=10,)

left_frame = tk.Frame(left_paned_window, bg="light gray")
left_frame.pack(fill="both", expand=False)

task_entry = tk.Entry(left_frame, font=("Arial", 12))
task_entry.pack(fill=tk.BOTH, padx=10, pady=10, expand=False)

add_task_button = tk.Button(
    left_frame, 
    text="Add Task", 
    command=add_task, 
    bg="green", 
    width=20, 
    height=2,
    fg="white",
    font=("Verdana", 14, "bold"),
    anchor="center"
)
add_task_button.pack(pady=10)
clear_task_button = tk.Button(
    left_frame, 
    text="Clear All", 
    command=clear_all_tasks, 
    bg="red", 
    width=20, 
    height=2,
    fg="white",
    font=("Verdana", 14, "bold"),
    anchor="center"
)
clear_task_button.pack(pady=10)

image_frame = tk.Frame(left_frame, bg="light gray")
image_frame.pack(fill="both", expand=True)

image_path = "C:/Users/hundal/Downloads/tasks-icon-17810(1).jpg"
image = Image.open(image_path)
image = image.resize((200, 200), Image.LANCZOS)
image = ImageTk.PhotoImage(image)

image_label = tk.Label(image_frame, image=image, bg="light gray")
image_label.image = image
image_label.pack(pady=10)

tk.Label(left_frame, text="", bg="light gray").pack(pady=10)

task_list_frame = tk.Frame(root, bg="light gray")
task_list_frame.grid(row=5, column=1, padx=10, pady=10,)

task_list_canvas = tk.Canvas(task_list_frame, bg="light gray")
task_list_canvas.pack(fill="both", expand=True, padx=10, pady=10,)

vertical_scrollbar = tk.Scrollbar(task_list_frame, orient="vertical", command=task_list_canvas.yview)
vertical_scrollbar.pack(side="right", fill="y")
task_list_canvas.configure(yscrollcommand=vertical_scrollbar.set)
task_list_canvas.bind("<Configure>", update_vertical_scrollbar)

horizontal_scrollbar = tk.Scrollbar(task_list_frame, orient="horizontal", command=task_list_canvas.xview)
horizontal_scrollbar.pack(side="bottom", fill="x")
task_list_canvas.configure(xscrollcommand=horizontal_scrollbar.set)

task_items_frame = tk.Frame(task_list_canvas, bg="light gray")
task_list_canvas.create_window((0, 0), window=task_items_frame, anchor="nw")

def _on_mousewheel(event):
    task_list_canvas.yview_scroll(-1*(event.delta//120), "units")
task_list_canvas.bind_all("<MouseWheel>", _on_mousewheel)

tasks = []
color_shades = ["#FFD700", "#98FB98", "#87CEFA", "#FFA07A"]

root.mainloop()
