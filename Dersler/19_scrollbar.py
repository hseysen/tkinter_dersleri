from random import choice, randint
import tkinter as tk


def rand_string(strlen):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join(choice(letters) for _ in range(strlen))


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("700x700")

fr = tk.LabelFrame(root, relief=tk.GROOVE)
fr.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

sc_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
sc_x.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.025)

sc_y = tk.Scrollbar(root, orient=tk.VERTICAL)
sc_y.place(relx=0.9, rely=0.1, relwidth=0.025, relheight=0.8)

t = tk.Text(fr, xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, wrap=tk.NONE)
t.pack(expand=True, fill=tk.BOTH)

sc_x.config(command=t.xview)
sc_y.config(command=t.yview)

for _ in range(100):
    t.insert(tk.INSERT, f"{rand_string(randint(1, 100))}\n")

root.mainloop()
