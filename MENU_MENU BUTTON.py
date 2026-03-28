import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Menu and Menubutton Example")
root.geometry("400x300")
# MENU BAR (Top Menu)
menubar = tk.Menu(root)
# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=lambda: messagebox.showinfo("New","New File Created"))
file_menu.add_command(label="Open", command=lambda: messagebox.showinfo("Open",
"File Opened"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: messagebox.showinfo("Cut",
"Cut Selected"))
edit_menu.add_command(label="Copy", command=lambda: messagebox.showinfo("Copy",
"Copied"))
edit_menu.add_command(label="Paste", command=lambda:
messagebox.showinfo("Paste", "Pasted"))
menubar.add_cascade(label="Edit", menu=edit_menu)
# Attach menu bar to window
root.config(menu=menubar)
# MENUBUTTON (Dropdown Button)
mb = tk.Menubutton(root, text="Options", relief=tk.RAISED)
mb.pack(pady=50)
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option 1", command=lambda:
messagebox.showinfo("Option 1", "You selected Option 1"))
mb.menu.add_command(label="Option 2", command=lambda:
messagebox.showinfo("Option 2", "You selected Option 2"))
mb.menu.add_command(label="Option 3", command=lambda:
messagebox.showinfo("Option 3", "You selected Option 3"))
root.mainloop()

