import tkinter as tk
from tkinter import messagebox
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create a list to store tasks
        self.tasks = []

        # Check if a file exists to load tasks
        self.load_tasks_from_file()

        # Create an entry widget to input tasks
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create a button to add tasks
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Create a button to view all tasks
        self.view_all_button = tk.Button(root, text="View All", command=self.view_all_tasks)
        self.view_all_button.grid(row=0, column=2, padx=10, pady=10)

        # Create a listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Create buttons to mark tasks as complete and delete tasks
        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Create a button to delete all tasks
        self.delete_all_button = tk.Button(root, text="Delete All", command=self.delete_all_tasks)
        self.delete_all_button.grid(row=2, column=2, padx=10, pady=10)

        # Display tasks in the listbox
        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Clear the entry field
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            task = self.tasks[task_index]
            completed_task = f"{task} (Completed)"
            self.tasks[task_index] = completed_task
            self.update_task_listbox()
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            del self.tasks[task_index]
            self.update_task_listbox()
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks(self):
        confirmed = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
        if confirmed:
            self.tasks = []
            self.update_task_listbox()
            self.save_tasks_to_file()

    def view_all_tasks(self):
        all_tasks = "\n".join(self.tasks)
        messagebox.showinfo("All Tasks", all_tasks)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks_from_file(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
