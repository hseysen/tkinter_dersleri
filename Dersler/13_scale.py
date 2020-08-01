import tkinter as tk


def b1click(scaleobj):
    print(scaleobj.get())


def b2click(scaleobj):
    scaleobj.set(100)


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")

value = tk.DoubleVar()
scale = tk.Scale(root, variable=value)
scale.pack()

# bd, relief, state, label, font, width, length, sliderlength
# activebackground, bg, fg
# scale.config(troughcolor="orange")

# scale.config(command=lambda v: print(v))

# scale.config(from_=15, to=35)

# scale.config(orient=tk.HORIZONTAL)
# scale.config(orient=tk.VERTICAL)

# scale.config(resolution=0.4)

# scale.config(from_=10, to=60, tickinterval=25, resolution=5)
#
# scale.config(showvalue=0)

b1 = tk.Button(root, text="Get", command=lambda: b1click(scale))
b1.pack()
b2 = tk.Button(root, text="Set", command=lambda: b2click(scale))
b2.pack()

root.mainloop()
