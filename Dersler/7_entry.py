from tkinter import *


root = Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")

f = ("Arial", 20)
n = Entry(root, font=f)         # bd, bg, fg, justify, relief, state, width
n.pack()


# n.config(selectbackground="green", selectforeground="white", selectborderwidth=20)
# n.config(show="*")

# b1 = Button(root, text="Enter", command=lambda: print(n.get()))
# b1.pack()
#
# b2 = Button(root, text="Delete first", command=lambda: n.delete(0))
# b2.pack()
#
# b3 = Button(root, text="Delete 1-3", command=lambda: n.delete(1, 3))
# b3.pack()
#
# b4 = Button(root, text="Cursor 5", command=lambda: n.icursor(5))
# b4.pack()
#
# b5 = Button(root, text="Insert salam", command=lambda: n.insert(0, "salam"))
# b5.pack()
#
# b6 = Button(root, text="Select_adjust 4", command=lambda: n.select_adjust(4))
# b6.pack()
#
# b7 = Button(root, text="Select Clear", command=lambda: n.select_clear())
# b7.pack()
#
# b8 = Button(root, text="Selection Present", command=lambda: print(n.selection_present()))
# b8.pack()
#
# b9 = Button(root, text="Select 2-6", command=lambda: n.select_range(2, 6))
# b9.pack()

root.mainloop()
