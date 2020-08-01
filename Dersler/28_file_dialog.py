import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog


ft = [("Text faylları", "*.txt"), ("Python faylları", "*.py *.pyw")]


def b1cmd():
    dr = filedialog.askdirectory(title="Qovluğu seçin")
    print(dr)


def b2cmd():
    fn = filedialog.askopenfilename(title="Bir fayl seçin", filetypes=ft)
    print(fn)


def b3cmd():
    fns = filedialog.askopenfilenames(title="Bir neçə fayl seçin", filetypes=ft)
    for fn in fns:
        print(fn)


def b4cmd():
    new_fn = filedialog.asksaveasfilename(title="Yadda saxlayın", filetypes=ft, defaultextension="*.*")
    print(new_fn)


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("700x700")


b1 = ttk.Button(root, takefocus=0, text="Qovluq", command=b1cmd)
b2 = ttk.Button(root, takefocus=0, text="Bir Fayl", command=b2cmd)
b3 = ttk.Button(root, takefocus=0, text="Çoxlu Fayl", command=b3cmd)
b4 = ttk.Button(root, takefocus=0, text="Yeni Fayl", command=b4cmd)
b1.pack()
b2.pack()
b3.pack()
b4.pack()


root.mainloop()
