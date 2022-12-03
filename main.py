
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
# /////////////////////////////////////////////////////
# creating window
window = tk.Tk()
window2 = tk.Tk()

window.attributes('-alpha', 0)
window2.attributes('-alpha', 0)
window.after(15000, lambda: window.destroy())
window2.after(15000, lambda: window2.destroy())
window.resizable(0, 0)
window2.resizable(0, 0)

# setting attribute
# window.geometry("1920x1080")
window.geometry(f'{1920}x{1080}+0+0')
window2.geometry(f'{1920}x{1080}+1920+0')
window.wm_attributes("-fullscreen", True)
window2.wm_attributes("-fullscreen", True)


image = Image.open('image.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(window, image=photo_image)
label.pack()

label1 = Label(window, image=photo_image)
label1.pack()


# live time


def my_time():
    time_s = strftime('%H:%M:%S %p %d %B %Y')
    l1.config(text=format(time_s))
    l1.after(1000, my_time)
    l2.config(text=format(time_s))
    l2.after(1000, my_time)


l1 = Label(window, font=('times', 26, 'bold'), foreground="red3")
l1.place(relx=1, rely=0, x=-38, y=65, anchor='ne')

l2 = Label(window2, font=('times', 26, 'bold'), foreground="red3")
l2.place(relx=1, rely=0, x=-38, y=65, anchor='ne')


my_time()
window.mainloop()
window2.mainloop()
# /////////////////////////////////////////////////////
