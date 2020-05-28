import os
import shutil
import tkinter as tk

folder_to_save = ["C:\\Users\\urbai\\Desktop\\jeu", "C:\\Users\\urbai\\Desktop\\Code", "C:\\Users\\urbai\\Desktop\\Ecole"]


def samefile(src_file, dst_file):
    try:
        if os.path.getsize(src_file) != os.path.getsize(dst_file):
            return False
        else:
            return True
    except:
        return False


def mergefolders(root_src_dir, root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            try:
                if samefile(src_file, dst_file):
                    pass
                else:
                    shutil.copy2(src_file, dst_dir)
            except FileNotFoundError:
                shutil.copy2(src_file, dst_dir)




mergefolders(folder_to_save[0], "Z:\\Bureau\\Backup\\Jeu")

mergefolders(folder_to_save[2], "Z:\\Bureau\\Backup\\Ecole")


mergefolders(folder_to_save[1], "Z:\\Bureau\\Backup\\Code")

Root = tk.Tk()
Root.iconbitmap("C:/Users/urbai/Desktop/folder.ico")
Root.title('Pi Sync')
img = tk.PhotoImage(file="C:/Users/urbai/Desktop/check.png")
canvas = tk.Canvas(Root, width=540, height=540)
canvas.create_image(20, 20, anchor='nw', image=img)
canvas.pack()
Root.mainloop()
