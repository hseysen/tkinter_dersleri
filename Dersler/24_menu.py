import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("300x300")


program_menu = tk.Menu(root)
root.config(menu=program_menu)

root.option_add("*tearOff", False)


file_menu = tk.Menu(program_menu)
program_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=lambda: print("New"))
file_menu.add_command(label="Open", command=lambda: print("Open"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: print("Exit"))


edit_menu = tk.Menu(program_menu)
program_menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=lambda: print("Cut"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))

root.mainloop()
