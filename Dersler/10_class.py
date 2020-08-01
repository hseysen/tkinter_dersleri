import tkinter as tk


class Application(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.configure_master()
        self.create_widgets()

    def configure_master(self):
        self.master.title("CIK Academy")
        self.master.iconbitmap("cik.ico")
        self.master.geometry("350x350")

    def create_widgets(self):
        self.testbutton = tk.Button(self, text="Click", command=self.onclick)
        self.testbutton.pack()

    @staticmethod
    def onclick():
        print("clicked")


def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()


if __name__ == "__main__":
    main()
