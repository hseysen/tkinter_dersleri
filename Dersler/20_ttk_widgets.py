import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("400x400")


b1 = tk.Button(root, text="Click")
b1.pack(side=tk.LEFT, padx=20)
b1.config(command=lambda: b1.config(state=tk.DISABLED))

b2 = ttk.Button(root, text="Click", takefocus=0)
b2.pack(side=tk.RIGHT, padx=20)
b2.config(command=lambda: b2.config(state=tk.DISABLED))


# b1.config(background="red", foreground="black", bd=3, font=("Arial", 14, "bold"),
#           activeforeground="white", activebackground="orange")


print("b1", b1.winfo_class())
print("b2", b2.winfo_class())

s = ttk.Style()
# s.theme_use("clam")
# print(s.theme_names())

# s.configure("TButton", background="blue", foreground="black", font=("Arial", 14, "bold"))

s.map('TButton',
      foreground=[('disabled', 'yellow'),
                  ('pressed', 'white'),
                  ('active', '#22222F')],
      background=[('disabled', 'gray'),
                  ('pressed', 'red'),
                  ('active', 'cyan')])

b3 = ttk.Button(root, text="Click", takefocus=0)
b3.pack(side=tk.RIGHT, padx=20)
b3.config(command=lambda: b3.config(state=tk.DISABLED))


root.mainloop()
