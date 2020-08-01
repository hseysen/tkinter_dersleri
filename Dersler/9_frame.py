import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("350x350")


fr = tk.LabelFrame(root, bg="red")
# fr.place(anchor=CENTER, relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)
fr.place(relx=0.25, rely=0.12, relwidth=0.43, relheight=0.2)

b = tk.Button(fr, text="Click", bg="black", fg="white")
b.place(anchor=tk.CENTER, relx=0.5, rely=0.5)

# font, bg, fg, relief, bd

root.mainloop()
