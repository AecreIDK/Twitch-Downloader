import customtkinter as ctk
import yt_dlp

# The Download List Queue for when downloading clips
DownloadQueue = []

class MassDownloadUrlList(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.TaskFrame = ctk.CTkScrollableFrame(master=self, width=150, height=100)
        self.TaskFrame.grid(row=0, column=0, padx=5, pady=5)

        self.ClipEntryBox = ctk.CTkEntry(master=self, placeholder_text="Enter a new url")
        self.ClipEntryBox.grid(row=0, column=1, padx=1, pady=1)

        self.AddToQueue = ctk.CTkButton(master=self, text="Add to queue", command=self.Add2Queue)
        self.AddToQueue.grid(row=1, column=1, padx=1, pady=1)

    def Add2Queue(self):
        url = self.ClipEntryBox.get()  # Get the URL from the entry box
        if url:  # Ensure the URL is not empty
            DownloadQueue.append(url)  # Append the URL to the queue

            self.UrlLabel = ctk.CTkLabel(self.TaskFrame, text=url, anchor="w", width=200)
            self.UrlLabel.grid(padx=0, pady=1)

            self.ClipEntryBox.delete(0, ctk.END)  # Clear the entry box
            self.ClipEntryBox.insert(0, "Added! Enter a new link or click 'Confirm' to download.")  # Feedback to user

class Tabs(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()
        
        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # Create Entry Box
        self.EntryBox = ctk.CTkEntry(master=self.tab("tab 1"), placeholder_text="Enter URL")
        self.EntryBox.grid(row=0, column=0, padx=20, pady=20)

        self.Confirm_Button = ctk.CTkButton(master=self.tab("tab 1"), text="Confirm", command=self.SingleDownload)
        self.Confirm_Button.grid(row=1, column=0, padx=20, pady=20)

        # TOP LEVEL FOR MULTIPLE DOWNLOAD
        self.toplevel_window = None

        self.Url_List_Downloader = ctk.CTkButton(master=self.tab("tab 2"), text="url list", command=self.open_toplevel)
        self.Url_List_Downloader.grid(row=0, column=0, padx=20, pady=20)

        self.DownloadButton = ctk.CTkButton(master=self.tab("tab 2"), text="Download", command=self.download)
        self.DownloadButton.grid(row=0, column=2, padx=20, pady=20)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = MassDownloadUrlList(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def SingleDownload(self):
        ydl_opts = {
            'format': 'best',  # Downloads the best available quality
        }

        url = self.EntryBox.get()

        # Example of using yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {url}")
        DownloadQueue.clear()  # Clear the queue after downloading
        self.EntryBox.delete(0, ctk.END)
        self.EntryBox.insert(0, "All downloads complete!")

    def download(self):
        ydl_opts = {
            'format': 'best',  # Downloads the best available quality
        }

        if not DownloadQueue:  # Check if the queue is empty
            print("No URLs in the queue")
        else:
            for url in DownloadQueue:
                # Example of using yt-dlp to download the video
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(f"Downloaded: {url}")
            DownloadQueue.clear()  # Clear the queue after downloading

class App(ctk.CTk):
    def __init__(self):  # Added default value for master
        super().__init__()
        
        self.Tab_View = Tabs(master=self)
        self.Tab_View.grid(row=0, column=0, padx=20, pady=20)


ctk.set_appearance_mode("dark")
app = App()
app.geometry("420x300")
app.mainloop()