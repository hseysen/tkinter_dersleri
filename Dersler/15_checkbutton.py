import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")


CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(root, text="Seçim 1", variable=CheckVar1, onvalue=1, offvalue=0)
C2 = tk.Checkbutton(root, text="Seçim 2", variable=CheckVar2, onvalue=1, offvalue=0)
C1.pack()
C2.pack()

# b = tk.Button(root, text="Click", command=lambda: print(CheckVar1.get(), CheckVar2.get()))
b = tk.Button(root, text="Click", command=lambda: C1.toggle())
b.pack()

root.mainloop()
