import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")


# v = tk.IntVar()
# v.set(1)
# w = tk.OptionMenu(root, v, 1, 2, 3, 4, 5)
# w.pack()

OPTIONS = ["Afrika",
           "Amerika",
           "Antarktida",
           "Avropa",
           "Asiya",
           "Avstraliya"]
v = tk.StringVar()
v.set(OPTIONS[0])
w = tk.OptionMenu(root, v, *OPTIONS)
w.pack()

b = tk.Button(root, text="Click", command=lambda: print(v.get()))
b.pack()

# relief, bd, bg, fg, activebackground, activeforeground, disabledforeground, state
# w.config(indicatoron=0)
w.config(direction="flush")
# above, below, flush, left, right

root.mainloop()
