import subprocess
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.entrythingy = tk.Entry(self)
        self.entrythingy.grid(row=0, column=0)

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("https://youtu.be/ZxhyCXHXJzI?si=bImTJ1ytWiFRqtrB")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        self.confirm_button = tk.Button(self, text="Confirm", command=self.download)
        self.confirm_button.grid(row=1, column=0)

    def download(self):
        url = self.contents.get()
        subprocess.run(f'yt-dlp {url}', shell=True)

root = tk.Tk()
myapp = App(root)

myapp.master.title("Dont Leak")
myapp.master.minsize(1000, 400)
myapp.master.maxsize(1000, 400)

myapp.mainloop()
