#!/usr/bin/env python
"""
Renames image files to label + file creation date + count 
Creation date is read if EXIF data is available
Otherwise get_exif_date returns nullstring
Example 1: img_140015.jpg -> label_2021_01_02_1_.jpg
Example 2: scann_15.jpg -> label.jpg
"""
import os
from tkinter import Tk, Label, Entry, Button, filedialog, scrolledtext, INSERT
from pathlib import Path
import PIL.Image

def get_exif_date(user_img: str) -> str:
    """
    """
    path = Path(LBL3.cget("text"))
    image = PIL.Image.open(path/user_img)
    exif_data = image._getexif()
    try:
        ldate = exif_data[306][:10]
        ldate = ldate.replace(':', '_')
        return ldate
    except TypeError as TE:
        print(TE)
        ldate = ""
        return ldate
    
def get_directory() -> None:
    """
    """
    user_dir = filedialog.askdirectory()
    LBL3.configure(text=user_dir)
    return user_dir

def main() -> None:
    """
    """
    path = Path(LBL3.cget("text"))
    count = 0
    label = LABEL_TXT1.get()
    files = [f for f in os.listdir(LBL3.cget("text")) \
            if os.path.isfile(os.path.join(LBL3.cget("text"), f))]
    for img in files:
        date = get_exif_date(img)
        count += 1
        ext = Path(img).suffix
        new_title = f"{label}_{date}_{count}{ext}"
        os.rename(path/img, path/new_title)
        #update GUI
        SCROLL_TXT.insert(INSERT, f"\n{img}\n renamed to: \n{new_title} \n")
    return

#############################

bg = "black"
fg = "white"

WINDOW = Tk()
WINDOW.title("EXIF 2 TITLE")
WINDOW.configure(background=bg)
WINDOW.geometry('400x400')

LBL_HEAD_TEXT = Label(WINDOW, 
    text="Label", 
    font=("Verdana", 12), 
    background=bg, 
    foreground=fg)
LBL_HEAD_TEXT.grid(column=0, row=1)

ENT_LABEL_ENTRY = Entry(WINDOW, 
    width=10, 
    font=("Verdana", 11))
ENT_LABEL_ENTRY.grid(column=0, row=2)

BTN_BROWSE= Button(WINDOW, 
    text="Browse Folder",
    command=get_directory,
    background=bg,
    foreground=fg,
    font=("Verdana", 11))
BTN_BROWSE.grid(column=0, row=5)

LBL_SELECTED_FOLDER = Label(WINDOW, 
    text="Selected folder:",
    font=("Verdana", 12), 
    background=bg, 
    foreground=fg)
LBL_SELECTED_FOLDER.grid(column=0, row=6)

LBL3 = Label(WINDOW, 
    text="...",
    font=("Verdana", 12), 
    background=bg, 
    foreground=fg)
LBL3.grid(column=0, row=7)

BTN_rename = Button(WINDOW, 
    text="Rename Files!",
    command=main,
    background=bg,
    foreground=fg,
    font=("Verdana", 11))
BTN_rename.grid(column=0, row=8)

SCROLL_TXT = scrolledtext.ScrolledText(WINDOW, 
    width=35, 
    height=8, 
    font=("Verdana", 11))
SCROLL_TXT.configure(background=bg, foreground=fg)
SCROLL_TXT.grid(column=0, row=9)

WINDOW.mainloop()
