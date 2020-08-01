from tkinter import *


root = Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")

f = ("Arial", 16, "bold")
u1 = Label(root, bg="red", text="Salam1", font=f)
u2 = Label(root, bg="blue", text="Salam2", font=f)
# u1.pack()
# u2.pack()
# u1.place(x=15, y=15, anchor=SE)
# u2.place(x=134, y=256, anchor=SE)
# u1.place(relx=0.3, rely=0.3, anchor=CENTER)
# u2.place(relx=0.7, rely=0.7, anchor=CENTER)
u1.place(relx=0.3, rely=0.3, relwidth=0.3, relheight=0.1, anchor=CENTER)
u2.place(relx=0.7, rely=0.7, relwidth=0.3, relheight=0.1, anchor=CENTER)


root.mainloop()
