from tkinter import *


def bindedfunction(event):
    print(event.__dict__)


root = Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")

u = Label(root, text="Salam", bg="blue", fg="orange")
u.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.5, anchor=N)

# u.bind("<Button-1>", bindedfunction)

root.bind("<Return>", bindedfunction)

root.mainloop()
