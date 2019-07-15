import pytube
#import pyperclip
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# video_link: str = input("Input Your Link: ")

# video_link = "https://www.youtube.com/watch?v=a1wvgLkyVfQ"
# yt = pytube.YouTube(video_link)
# videos = yt.streams.first()
# videos.download('I:\\Opening Video')

# function to download
def download():
    if not link_input:
        messagebox.showerror("Error", "Link is empty !!")
    else:
        video_link = link_input.get()
        yt = pytube.YouTube(video_link)
        videos = yt.streams.first()
        videos.download('C:\\Users\\Michael\\Opening Video')


def cancel():
    root.destroy()


# Main
# create GUI
root = Tk()

# Title for program
root.title("Youtube Downloader")

# entry to show
link = Label(root, text="Youtube Link")
link.grid(row=0)
link_input = Entry(root)
link_input.grid(row=0, column=1)

# create download button
download_butt = Button(root, text="Download", command=download)
download_butt.grid(row=1)
cancel_button = Button(root, text="Cancel", command=cancel)
cancel_button.grid(row=1, column=1)

root.mainloop()
