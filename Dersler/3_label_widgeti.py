from tkinter import *


root = Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")


t = StringVar()
t.set("Salam\nSalam Salam\nSalam Salam Salam")
f = ("Times New Roman", 16, "italic")

u = Label(root, textvariable=t, font=f, justify=RIGHT, relief=SUNKEN)
# relief: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
u.pack()

u.config(bg="orange", fg="blue")
# u.config(bg="#FF00E7", fg="#FFF300")

# u.config(width=25, height=5)
# u.config(anchor=NW)             # NW, N, NE, SW, S, SE, W, E, CENTER

root.mainloop()
