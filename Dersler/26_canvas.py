import tkinter as tk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("600x600")
root.resizable(False, False)

canv = tk.Canvas(root, bg="gray", width=600, height=600)
canv.pack()

# line = canv.create_line(0, 0, 350, 500, width=5, fill="blue", arrow="last")
# rect = canv.create_rectangle(50, 50, 100, 100, width=10, outline="red", fill="orange")
# text = canv.create_text(250, 250, text="HELLO", font=("Consolas", 32), fill="green")
# oval = canv.create_oval(200, 200, 300, 400, width=10, outline="green", fill="blue", activefill="red")
# poly = canv.create_polygon(100, 100, 100, 250, 300, 250, width=10, outline="red", fill="blue")
arc = canv.create_arc(100, 100, 300, 300, extent=135, start=0, width=10, outline="orange", fill="yellow")


root.mainloop()
