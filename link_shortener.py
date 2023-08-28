import pyshorteners
from tkinter import *
from PIL import Image, ImageTk

def short():
    Url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(Url)
    entry2.insert(END, s)

window = Tk()
window.geometry("400x270")


bg_image = Image.open(r"C:\Intel\blur(img).jpg") 
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


Label(window,text="Enter  Your  Url  Link", font="impack 15 bold", bg="black", fg="white").pack(fill="x")

entry1 = Entry(window, font="10", bd=2, width=34)
entry1.pack(pady=30)


Button(window, text="Click Me", font="impack 12 bold", bg="blue", fg="white", width="10", command=short).pack()


entry2 = Entry(window, font="impack 16 bold", bg="grey", width=24, bd=0)
entry2.pack(pady=30)

mainloop()