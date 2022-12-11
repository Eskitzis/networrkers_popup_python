import tkinter
import tkinter as tk
import webbrowser
from tkinter import *
from PIL import Image, ImageTk
from time import strftime

# /////////////////////////////////////////////////////
# creating window
window = tk.Tk()
window.configure(bg='#333333')
window.title("Networrkers")
window2 = tk.Tk()
window2.configure(bg='#333333')
window2.title("Networrkers")
window3 = tk.Tk()
window3.configure(bg='#333333')
window3.title("Networrkers")

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

watermark = Label(window, text='Powered by Networrkers', bg='#333333', fg="#FF3399", font=("Arial", 20))
watermark.place(relx = 0.0, rely = 1.0, x=10, y=-10, anchor ='sw')

welcome_tag = Label(window, text='| WELCOME |', bg='#333333', fg="#FFFFFF", font=("Arial", 40))
welcome_tag.place(relx = 0, rely = 0,x=10,y=45, anchor ='nw')

warning_message = Label(window, text='BITTE DAS ABSTEMPELN NICHT VERGESSEN', bg='#333333', fg="#FFFFFF", font=("Arial", 45))
warning_message.place(relx = 0.5,rely = 0.5,anchor = 'center')

greeting_message = Label(window, text='| Dein Team wünscht dir einen schönen Tag |', bg='#333333', fg="#FFFFFF", font=("Arial", 30))
greeting_message.place(relx = 0.5,rely = 0.5,y=70,anchor = 'center')

#url = 'http://networrkers.de'
#webbrowser.open(url)

# live time


def my_time():
    time_s = strftime('%H:%M:%S %p %d %B %Y')
    time_label.config(text=format(time_s))
    time_label.after(1000, my_time)


time_label = Label(window, font=('times', 30, 'bold'), bg='#333333',foreground="red3")
time_label.place(relx=1, rely=0, x=-38, y=45, anchor='ne')


my_time()
window.mainloop()
window2.mainloop()
window3.mainloop()
# /////////////////////////////////////////////////////
