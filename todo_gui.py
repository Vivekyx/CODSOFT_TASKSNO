import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path

tasks = []

TASK_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    global tasks

    if TASK_FILE.exists():
        try:
            with open(TASK_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, OSError):
            tasks = []


def save_tasks():
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        tasks.append(task)
        save_tasks()
        task_entry.delete(0, tk.END)
        show_tasks()


def show_tasks():
    task_list.delete(0, tk.END)

    for number, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{number}. {task}")


def delete_task():
    selected = task_list.curselection()

    if selected:
        tasks.pop(selected[0])
        save_tasks()
        show_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task first")


def update_task():
    selected = task_list.curselection()
    new_task = task_entry.get().strip()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first")
    elif new_task == "":
        messagebox.showwarning("Warning", "Enter the new task")
    else:
        tasks[selected[0]] = new_task
        save_tasks()
        task_entry.delete(0, tk.END)
        show_tasks()


window = tk.Tk()
window.title("Vivek's To-Do List")
window.geometry("500x500")
window.config(bg="#f0f4f8")

heading = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#f0f4f8",
    fg="#263859"
)
heading.pack(pady=20)

task_entry = tk.Entry(
    window,
    font=("Arial", 13),
    width=30
)
task_entry.pack(pady=10)

add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task,
    bg="#2563eb",
    fg="white",
    width=18
)
add_button.pack(pady=5)

task_list = tk.Listbox(
    window,
    width=40,
    height=12,
    font=("Arial", 12)
)
task_list.pack(pady=15)

update_button = tk.Button(
    window,
    text="Update Task",
    command=update_task,
    bg="#f59e0b",
    fg="white",
    width=18
)
update_button.pack(pady=5)

delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task,
    bg="#dc2626",
    fg="white",
    width=18
)
delete_button.pack(pady=5)

load_tasks()
show_tasks()

window.mainloop()