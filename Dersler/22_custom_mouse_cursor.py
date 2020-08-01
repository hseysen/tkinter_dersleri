import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title("CIK Academy")
root.iconbitmap("cik.ico")
root.geometry("600x250")

cursors = ['arrow', 'based_arrow_down', 'based_arrow_up', 'boat', 'bogosity',
           'bottom_left_corner', 'bottom_right_corner', 'bottom_side',
           'bottom_tee', 'box_spiral', 'center_ptr', 'circle', 'clock',
           'coffee_mug', 'cross', 'cross_reverse', 'crosshair', 'diamond_cross',
           'dot', 'dotbox', 'double_arrow', 'draft_large', 'draft_small',
           'draped_box', 'exchange', 'fleur', 'gobbler', 'gumby', 'hand1',
           'hand2', 'heart', 'icon', 'iron_cross', 'left_ptr', 'left_side',
           'left_tee', 'leftbutton', 'll_angle', 'lr_angle', 'man',
           'middlebutton', 'mouse', 'pencil', 'pirate', 'plus', 'question_arrow',
           'right_ptr', 'right_side', 'right_tee', 'rightbutton', 'rtl_logo',
           'sailboat', 'sb_down_arrow', 'sb_h_double_arrow', 'sb_left_arrow',
           'sb_right_arrow', 'sb_up_arrow', 'sb_v_double_arrow', 'shuttle',
           'sizing', 'spider', 'spraycan', 'star', 'target', 'tcross',
           'top_left_arrow', 'top_left_corner', 'top_right_corner', 'top_side',
           'top_tee', 'trek', 'ul_angle', 'umbrella', 'ur_angle', 'watch',
           'xterm', 'X_cursor']

current = 0


def change(label):
    global current
    if current == len(cursors) - 1:
        current = -1
    current += 1
    label.config(cursor=cursors[current])
    label.config(text="{:15}{:10}".format(cursors[current], " "))


u = ttk.Label(root, font=("Arial", 18, "bold"), background="cyan")
u.pack(pady=20, fill=tk.X)

u.config(cursor=cursors[current])
u.config(text=f"{cursors[current]}")
root.bind("<c>", lambda event: change(u))


root.mainloop()