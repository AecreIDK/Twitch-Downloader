import customtkinter as ctk

# Initialize the customtkinter app
ctk.set_appearance_mode("System")  # Can be set to "Light" or "Dark" as well
ctk.set_default_color_theme("blue")  # Optional: Sets the theme color

class NotepadApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main window settings
        self.title("CustomTkinter Notepad List")
        self.geometry("400x500")

        # Frame for the list of tasks
        self.task_frame = ctk.CTkScrollableFrame(self, width=350, height=300)
        self.task_frame.pack(pady=20)

        # Entry field and add button for new tasks
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Enter a new task")
        self.task_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Button to clear all tasks
        self.clear_button = ctk.CTkButton(self, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

        # Storage for task labels
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            # Create a task label and delete button
            task_label = ctk.CTkLabel(self.task_frame, text=task_text, anchor="w", width=280)
            task_label.pack(pady=2, fill="x")

            delete_button = ctk.CTkButton(self.task_frame, text="Delete", width=50, command=lambda: self.remove_task(task_label, delete_button))
            delete_button.pack(pady=2)

            self.tasks.append((task_label, delete_button))
            self.task_entry.delete(0, "end")

    def remove_task(self, task_label, delete_button):
        task_label.destroy()
        delete_button.destroy()

    def clear_tasks(self):
        for task, button in self.tasks:
            task.destroy()
            button.destroy()
        self.tasks = []

# Run the app
if __name__ == "__main__":
    app = NotepadApp()
    app.mainloop()
