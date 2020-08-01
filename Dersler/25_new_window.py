import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Application(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master = master
        self.configure_master()
        self.create_widgets()

    def configure_master(self):
        self.master.title("CIK Academy")
        self.master.iconbitmap("cik.ico")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

    def create_widgets(self):
        self.openbutton = ttk.Button(self.master, takefocus=0, text="Open window", command=self.openwindow)
        self.openbutton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # def openwindow(self):
    #     try:
    #         if self.newwindow.winfo_exists():
    #             return
    #     except:
    #         pass
    #     self.newwindow = tk.Toplevel()
    #     self.newwindow.title("New Window")
    #     self.newwindow.iconbitmap("cik.ico")
    #     self.image_to_display = ImageTk.PhotoImage(Image.open("DogPhotos/dog1.jpg"))
    #     self.picture = ttk.Label(self.newwindow, image=self.image_to_display)
    #     self.picture.pack()
    #     self.closebutton = ttk.Button(self.newwindow, takefocus=0, text="Close window", command=self.closewindow)
    #     self.closebutton.pack()
    #
    # def closewindow(self):
    #     self.newwindow.destroy()

    def openwindow(self):
        try:
            if self.newwindow.winfo_exists():
                return
        except:
            pass
        self.newwindow = NewWindow()


class NewWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("New Window")
        self.iconbitmap("cik.ico")
        self.create_widgets()

    def create_widgets(self):
        self.image_to_display = ImageTk.PhotoImage(Image.open("../DogPhotos/dog1.jpg"))
        self.picture = ttk.Label(self, image=self.image_to_display)
        self.picture.pack()
        self.closebutton = ttk.Button(self, takefocus=0, text="Close window", command=self.closewindow)
        self.closebutton.pack()

    def closewindow(self):
        self.destroy()


def main():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()


if __name__ == "__main__":
    main()
