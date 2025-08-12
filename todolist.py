import tkinter as tk
from tkinter import font as tkfont


def add_task():
    """Add the task from the entry widget to the listbox."""
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


def toggle_task(event):
    """Strike through or unstrike the selected task."""
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    item_font = item_fonts.get(index)
    if item_font is None:
        item_font = tkfont.Font(listbox, listbox.cget("font"))
        item_fonts[index] = item_font
    item_font.configure(overstrike=0 if item_font.actual()["overstrike"] else 1)
    listbox.itemconfig(index, font=item_font)


root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

listbox = tk.Listbox(root, width=50, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
listbox.bind("<Double-Button-1>", toggle_task)

item_fonts = {}

root.mainloop()
