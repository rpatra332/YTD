import tkinter as tk
from tkinter import filedialog, messagebox, Entry, Label, Button, StringVar, GROOVE, RAISED

from pytube import YouTube
from pytube.exceptions import RegexMatchError


def gui_components():
    intro_label = Label(root, text='YouTube Video Downloader', padx=10, pady=15, font=('SegoeUI', 14, 'bold'),
                        bg='whitesmoke', fg='blue')
    intro_label.grid(row=1, column=1, padx=5, pady=5)

    link_label = Label(root, text='Video Link : ', padx=5, pady=5, font='SegoeUI 14', bg='whitesmoke', fg='black')
    link_label.grid(row=2, column=0, padx=5, pady=5)

    destination_label = Label(root, text='Destination :', padx=5, pady=5, font='SegoeUI 14', bg='whitesmoke',
                              fg='black')
    destination_label.grid(row=3, column=0, padx=5, pady=5)

    link_text = Entry(root, textvariable=video_link, width=49)
    link_text.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

    destination_path_text = Entry(root, textvariable=destination, width=35)
    destination_path_text.grid(row=3, column=1, padx=5, pady=5)

    browse_button = Button(root, text='Browse', command=browse, width=10, bg='whitesmoke', relief=GROOVE)
    browse_button.grid(row=3, column=2, padx=1, pady=1)

    download_button = Button(root, text='Download Video', command=download, width=20, bg='blue2', fg='white', padx=15,
                             pady=10,
                             relief=RAISED, font=('Georgia', 14))
    download_button.grid(row=4, column=1, padx=20, pady=20)


def browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    destination.set(download_directory)


def callback():
    messagebox.showerror("Message", "Video link or Destination Wrong!")
    pass


def download():
    try:
        # ask for the link from user
        yt = YouTube(video_link.get())

        # Getting the highest resolution possible
        ys = yt.streams.get_highest_resolution()

        # Starting download
        print("Downloading...")
        ys.download(destination.get())
        print("Download completed!!")

        messagebox.showinfo("Successful", f"SUCCESSFULLY DOWNLOADED AND SAVED IN \n{str(destination.get())}")

    except RegexMatchError:
        print("Wrong inputs for downloads")
        callback()


root = tk.Tk()

root.geometry("520x280")
root.resizable(False, False)
root.title('YouTube Video Downloader')
root.config(bg='whitesmoke')
root.iconbitmap("./image-assets/icon.ico")

video_link = StringVar()
destination = StringVar()

gui_components()

root.mainloop()
