import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
# /////////////////////////////////////////////////////
# creating window
window = tk.Tk()
window2 = tk.Tk()
window3 = tk.Tk()

window.after(15000, lambda: window.destroy())
window2.after(15000, lambda: window2.destroy())
window3.after(15000, lambda: window3.destroy())
window.resizable(height=None, width=None)
window2.resizable(height=None, width=None)
window3.resizable(height=None, width=None)

# getting screen size
scrW = window.winfo_screenwidth()
scrH = window.winfo_screenheight()

# setting attribute
window.geometry("1920x1080+0+0")
window2.geometry("1920x1080+%d+0" % scrW)
window3.geometry("1920x1080-%d-0" % scrW)
window.attributes("-fullscreen", True)
# window2.attributes("-fullscreen", True)
# window3.attributes("-fullscreen", True)

image = Image.open(r"C:\Users\anton\PycharmProjects\networrkers_popup_python\image.png")
photo_image = ImageTk.PhotoImage(image)
label = Label(window, image=photo_image)
label.pack()

# live time


def my_time():
    time_s = strftime('%H:%M:%S %p %d %B %Y')
    l1.config(text=format(time_s))
    l1.after(1000, my_time)


l1 = Label(window, font=('times', 25, 'bold'), foreground="red3")
l1.place(relx=1, rely=0, x=-38, y=65, anchor='ne')


my_time()
window.mainloop()
window2.mainloop()
window3.mainloop()
# /////////////////////////////////////////////////////
