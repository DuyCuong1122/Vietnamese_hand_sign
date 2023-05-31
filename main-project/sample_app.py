import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk
import shutil
import os
import numpy as np

#UI
win_desktop = tk.Tk()
win_desktop.geometry('1080x720')
win_desktop.title('Image Checker App')
win_desktop.resizable(width=False, height=False)

def menu_popup(e):
    menu_bar.tk_popup(x=e.x_root, y=e.y_root)

images_list = []
images_vars = []

def display_images(index):
    image_display_lb_1.config(image=images_list[index][1])
def load_images():
    dir_path = tk_file.askdirectory()
    images_files = os.listdir(dir_path)
    for r in range(0, len(images_files)):
        images_list.append([
            ImageTk.PhotoImage(Image.open(dir_path + '/' + images_files[r]).resize((80,80), Image.ANTIALIAS)),
            ImageTk.PhotoImage(Image.open(dir_path + '/' + images_files[r]).resize((300,300), Image.ANTIALIAS))
        ])

        images_vars.append(f'img_{r}')

    for n in range(len(images_vars)):
        globals()[images_vars[n]] = tk.Button(slider, image=images_list[n][0], bd=0,
                                              command=lambda n=n:display_images(n))
        globals()[images_vars[n]].pack(side=tk.LEFT)

#Menu button
menu_btn = tk.Button(win_desktop, text='=', bd=0, font=('Bold', 25))
menu_btn.pack(side=tk.TOP, anchor=tk.W, pady=5, padx=10)
menu_btn.bind('<Button-1>', menu_popup)
menu_bar = tk.Menu(win_desktop, tearoff=False)
menu_bar.add_command(label='Open Folder', command=load_images)

#Image display
image_display_lb_1 = tk.Label(win_desktop)
image_display_lb_1.pack(anchor=tk.W, pady=50, padx=50)

canvas = tk.Canvas(win_desktop, height=80, width=720)
canvas.pack(side=tk.BOTTOM, fill=tk.X)

x_scroll_bar = ttk.Scrollbar(win_desktop, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = ttk.Frame(canvas)
canvas.create_window((0,0), window=slider, anchor=tk.NW)
win_desktop.mainloop()