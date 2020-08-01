from tkinter import *


# Argumentsiz funksiya
def button_click1():
    print("Duymeye basildi")


# Argumentli funksiya
def button_click2(x):
    print("x =", x)


root = Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")


f = ("Helvetica", 16, "bold italic")
b = Button(root, text="Click", font=f)
b.pack()

# b.config(command=button_click1)
# b.config(command=lambda: button_click2(5))

# b.config(bd=5)

# justify, relief, height, width parametrlərini də yoxlaya bilərsiniz
b.config(bg="blue", fg="orange")
b.config(activebackground="gray", activeforeground="red")

b.config(state=DISABLED)            # NORMAL


root.mainloop()
