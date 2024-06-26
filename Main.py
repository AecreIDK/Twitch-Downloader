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

        #self.link = tk.Label(self, text="Supported Sites", fg="Blue", cursor="Hand2")
        #self.link.grid(row=2,column=2)
        #self.link.bind("<Button-1>", lambda e: self.URL_Open("Google.com"))

    def download(self):
        url = self.contents.get()
        subprocess.run(f'yt-dlp {url}', shell=True)

    #def URL_Open(self, url):
    #    webbrowser.open_new(url)

root = tk.Tk()
myapp = App(root)

myapp.master.title("Dont Leak")
myapp.master.minsize(1000, 400)
myapp.master.maxsize(1000, 400)

myapp.mainloop()
