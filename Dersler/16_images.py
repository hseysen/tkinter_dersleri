import tkinter as tk
from PIL import Image, ImageTk
import os


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("700x700")

# dog_photo = ImageTk.PhotoImage(Image.open("DogPhotos/dog1.jpg"))
#
# u = tk.Label(root, text="Hello", image=dog_photo, compound="right")
# b = tk.Button(root, text="Click", image=dog_photo, compound="right", command=lambda: print("Clicked"))
# c = tk.Checkbutton(image=dog_photo)
# u.pack()
# b.pack()
# c.pack()

cs = []
cvs = []
iobjs = []
for img in os.listdir("../DogPhotos"):
    iobjs.append(ImageTk.PhotoImage(Image.open(os.path.join("../DogPhotos", img))))
    cvs.append(tk.IntVar())
    cs.append(tk.Checkbutton(root, image=iobjs[-1], variable=cvs[-1], onvalue=1, offvalue=0))
    cs[-1].pack()

root.mainloop()
