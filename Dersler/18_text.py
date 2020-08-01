import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("700x700")

# t = tk.Text(root, height=10, width=30)
# t.pack()
#
# t.insert(tk.INSERT, "Sətir 1\n")
# t.insert(tk.INSERT, "Sətir 2\n")
#
# t.insert(2.5, "INSERT")

# state, background, foreground, selectbackground, selectforeground
# relief, bd, font, padx, pady
# t.config(insertontime=200, insertofftime=0)
# t.config(insertwidth=5, insertbackground="green")

# t.tag_config("t1", background="yellow", foreground="blue")
# t.tag_add("t1", 1.0, 1.3)


normfont = ("Times New Roman", 14)
boldfont = ("Times New Roman", 14, "bold")
t = tk.Text(root, height=10, width=30)
t.pack()
t.config(background="#333333", foreground="white", font=normfont)
t.tag_config("BoldFont", font=boldfont)

b = tk.Button(root, text="Bold", command=lambda: t.tag_add("BoldFont", tk.SEL_FIRST, tk.SEL_LAST))
b.pack()

# t.config(spacing1=30)
# t.config(spacing2=30)
# t.config(spacing3=30)

t.config(wrap=tk.NONE)  # tk.CHAR

root.mainloop()
