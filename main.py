import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from time import strftime

# creating window
window = tk.Tk()
window.after(15000, lambda: window.destroy())
# window.resizable(0,0)

# setting attribute
window.attributes('-fullscreen', True)

image = Image.open('image.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(window, image=photo_image)
label.pack()

# live time


def my_time():
    time_s = strftime('%H:%M:%S %p %d %B %Y')
    l1.config(text="{}".format(time_s))
    l1.after(1000, my_time)


l1 = Label(window, font=('times', 25, 'bold'))
l1.place(relx=1, rely=0, x=-15, y=50, anchor='ne')

my_time()
window.mainloop()
