import tkinter as tk


def radioclick(var):
    print(var.get())


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")

# v = tk.IntVar()
# r1 = tk.Radiobutton(root, text="Seçim 1", variable=v, value=1)
# r2 = tk.Radiobutton(root, text="Seçim 2", variable=v, value=2)
# r3 = tk.Radiobutton(root, text="Seçim 3", variable=v, value=3)
# r1.pack()
# r2.pack()
# r3.pack()

# b = tk.Button(root, text="Click", command=lambda: print(v.get()))
# b.pack()

# r1.config(command=lambda: radioclick(v))
# r2.config(command=lambda: radioclick(v))
# r3.config(command=lambda: radioclick(v))

# r1.config(indicatoron=0)
# r2.config(indicatoron=0)
# r3.config(indicatoron=0)

MODES = (("Azərbaycanca", "az"),
         ("English", "en"),
         ("Türkçe", "tr"),
         ("Français", "fr"))
rbs = []
v = tk.StringVar()
v.set(None)
for t, m in MODES:
    rbs.append(tk.Radiobutton(root, text=t, variable=v, value=m, command=lambda: radioclick(v)))
    rbs[-1].pack()


root.mainloop()
