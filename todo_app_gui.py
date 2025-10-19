# todo_app_gui.py
# GUI To-Do List App using Tkinter

import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        # All Content box removed; no additional refresh needed
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        listbox.delete(index)
        tasks.remove(task)
        # All Content box removed; no additional refresh needed
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()
        # All Content box removed; no additional refresh needed

root = tk.Tk()
root.title("\ud83d\udcdd Python To-Do List")
root.geometry("340x460")

# Outer frame with visible border around the app content (smaller/thinner)
outer_frame = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=4, pady=4)
outer_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

# Inner frame (no explicit background color)
inner_frame = tk.Frame(outer_frame, padx=10, pady=10)
inner_frame.pack(fill=tk.BOTH, expand=True)

title = tk.Label(inner_frame, text="To-Do List", font=("Arial", 30, "bold"))
title.pack(pady=10)

entry = tk.Entry(inner_frame, width=40, bg="#B3BFFF", fg="#000000")
entry.pack(pady=10)

tk.Button(inner_frame, text="Add Task", width=15, command=add_task).pack(pady=5)
tk.Button(inner_frame, text="Delete Task", width=15, command=delete_task).pack(pady=5)
tk.Button(inner_frame, text="Clear All", width=15, command=clear_tasks).pack(pady=5)

listbox = tk.Listbox(inner_frame, width=60, height=20, bg="#B3BFFF", fg="#000000")
listbox.pack(pady=10)
root.mainloop()
