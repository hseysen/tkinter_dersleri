import tkinter as tk
from tkinter import messagebox
from math import sqrt, factorial

APPNAME = "Calculator"
ICONLOC = "cik.ico"
SIZE = (368, 370)
ENCODING = "utf-8"
SQRTSYMBOL = "\u221A"
MULTIPLYSYMBOL = "\u00D7"
DIVISIONSYMBOL = "\u00F7"
DELSYMBOL = "\u2190"
OUTSYMBOL = "\u2191"
STICKYTEXT = "NWSE"
TEXTFONT = ("Consolas", 24)
ENTRYBG = "#96999E"
ENTRYFG = "black"
BUTTONBG = "#63728A"
BUTTONFG = "white"
BUTTONACTIVEBG = "slate gray"

POSSIBLE_ERRORS = {
    "division by zero": "Sıfra bölmə əməliyyatı",
    "math domain error": "Riyazi əməliyyat təyin olunmayıb"
}


class Calculator(tk.LabelFrame):
    OUTPUTFILE = "output.txt"

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure_master()
        self.pack()
        self.create_widgets()

    def configure_master(self):
        self.master.title(APPNAME)
        self.master.iconbitmap(ICONLOC)
        self.master.geometry("{}x{}".format(*SIZE))
        self.master.resizable(False, False)

    def create_widgets(self):
        self.entrybox = tk.Entry(self, font=TEXTFONT, bd=1, width=20)
        self.entrybox.grid(row=0, column=0, columnspan=5)
        self.entrybox.config(state=tk.DISABLED, disabledbackground=ENTRYBG, disabledforeground=ENTRYFG)

        self.buttons = []
        buttoninfos = [("%", 1, 0, lambda: self.add_character("%")),
                       (SQRTSYMBOL, 2, 0, lambda: self.add_character("{}(".format(SQRTSYMBOL))),
                       ("^", 3, 0, lambda: self.add_character("^")),
                       ("!", 4, 0, lambda: self.add_character("factorial(")),
                       (".", 5, 0, lambda: self.add_character(".")),
                       (OUTSYMBOL, 1, 1, self.output_current),
                       ("C", 1, 2, self.clear_entry),
                       (DELSYMBOL, 1, 3, self.erase_one),
                       ("0", 5, 2, lambda: self.add_character("0")),
                       ("1", 4, 1, lambda: self.add_character("1")),
                       ("2", 4, 2, lambda: self.add_character("2")),
                       ("3", 4, 3, lambda: self.add_character("3")),
                       ("4", 3, 1, lambda: self.add_character("4")),
                       ("5", 3, 2, lambda: self.add_character("5")),
                       ("6", 3, 3, lambda: self.add_character("6")),
                       ("7", 2, 1, lambda: self.add_character("7")),
                       ("8", 2, 2, lambda: self.add_character("8")),
                       ("9", 2, 3, lambda: self.add_character("9")),
                       ("+", 1, 4, lambda: self.add_character("+")),
                       ("-", 2, 4, lambda: self.add_character("-")),
                       (MULTIPLYSYMBOL, 3, 4, lambda: self.add_character(MULTIPLYSYMBOL)),
                       (DIVISIONSYMBOL, 4, 4, lambda: self.add_character(DIVISIONSYMBOL)),
                       ("=", 5, 4, self.calculate),
                       ("(", 5, 1, lambda: self.add_character("(")),
                       (")", 5, 3, lambda: self.add_character(")"))]

        for displaytext, i, j, cmd in buttoninfos:
            self.buttons.append(self.create_button(displaytext, i, j, cmd))

        self.keyboard_bind()

    def create_button(self, displaytext, i, j, cmd):
        b = tk.Button(self, text=displaytext, font=TEXTFONT, command=cmd)
        b.grid(row=i, column=j, sticky=STICKYTEXT)
        b.config(bg=BUTTONBG, fg=BUTTONFG, activebackground=BUTTONACTIVEBG)
        return b

    def add_character(self, character):
        self.entrybox.configure(state=tk.NORMAL)
        self.entrybox.insert(tk.END, character)
        self.entrybox.configure(state=tk.DISABLED)
        self.entrybox.focus()

    def clear_entry(self):
        self.entrybox.configure(state=tk.NORMAL)
        self.entrybox.delete(0, tk.END)
        self.entrybox.configure(state=tk.DISABLED)

    def erase_one(self):
        self.entrybox.configure(state=tk.NORMAL)
        current_entry = self.entrybox.get()
        self.clear_entry()
        self.add_character(current_entry[:-1])
        self.entrybox.configure(state=tk.DISABLED)

    def calculate(self):
        self.entrybox.configure(state=tk.NORMAL)
        calculation = self.entrybox.get()
        calculation = calculation.replace(SQRTSYMBOL, "sqrt")
        calculation = calculation.replace(MULTIPLYSYMBOL, "*")
        while "**" in calculation:
            calculation = calculation.replace("**", "*")
        calculation = calculation.replace("^", "**")
        calculation = calculation.replace(DIVISIONSYMBOL, "/")
        calculation = calculation.rstrip("=")
        if len(calculation) == 0:
            calculation = "0"
        try:
            res = eval(calculation)
        except SyntaxError:
            desc = "Riyazi hesablama sintaksisində səhv var!"
            messagebox.showerror("Xəta baş verdi!", "Hesablamada xəta var!", detail=desc)
        except Exception as e:
            try:
                desc = POSSIBLE_ERRORS[str(e)]
            except KeyError:
                desc = None
            messagebox.showerror("Xəta baş verdi!", "Hesablamada xəta var!", detail=desc)
        else:
            self.show_answer(res)
        self.entrybox.configure(state=tk.DISABLED)

    def show_answer(self, ans):
        self.entrybox.delete(0, tk.END)
        ans = str(ans)
        if len(ans) > 15:
            ans = "{:.10e}".format(float(ans))
        else:
            if "." in ans:
                ans = str(ans).rstrip("0").rstrip(".")
            if len(ans) == "0":
                ans = "0"
        self.entrybox.insert(0, ans)

    def keyboard_bind(self):
        num_keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        op_keys = ["+", "-", "*", "/", "=", "%", ".", "(", ")"]
        special_op_keys = {
            "!": "factorial(",
            "s": "{}(".format(SQRTSYMBOL),
            "p": "^"
        }
        other_keys = {
            "<Return>": self.calculate,
            "<BackSpace>": self.erase_one,
            "c": self.clear_entry
        }

        for key in num_keys:
            self.master.bind(key, lambda event, c=key: self.add_character(c))
        for key in op_keys:
            self.master.bind(key, lambda event, c=key: self.add_character(c))
        for key in special_op_keys:
            self.master.bind(key, lambda event, c=special_op_keys[key]: self.add_character(c))
        for key in other_keys:
            self.master.bind(key, lambda event, func=other_keys[key]: func())

        self.entrybox.bind("<Left>", lambda event: self.entrybox.xview_scroll(-1, tk.UNITS))
        self.entrybox.bind("<Right>", lambda event: self.entrybox.xview_scroll(1, tk.UNITS))

    def output_current(self):
        with open(Calculator.OUTPUTFILE, "a", encoding=ENCODING) as f:
            self.entrybox.configure(state=tk.NORMAL)
            current = self.entrybox.get()
            self.entrybox.configure(state=tk.DISABLED)
            if current == " ":
                return
            f.write(current + "\n")


def main():
    root = tk.Tk()
    calc = Calculator(root)
    calc.mainloop()


if __name__ == "__main__":
    main()
