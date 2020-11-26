from tkinter import *
from tkinter.ttk import Progressbar
from downloader import download_video, download_audio
import subprocess

root = Tk()
root.title("Youtube Downloader")
first_click=True

def clear_all():
    url_entry.delete(0, "end")

def get_video():
    import time
    url = url_entry.get()
    time.sleep(1)
    download_video(str(url))
    url_entry.delete(0, "end")
    url_entry.config(foreground="green")
    url_entry.insert("0", "FINISHED DOWNLOADING!")

def get_audio():
    url = url_entry.get()
    download_audio(str(url))
    url_entry.delete(0, "end")
    url_entry.config(foreground="green")
    url_entry.insert("0", "FINISHED DOWNLOADING!")


def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click

    if first_click: # if this is the first time they clicked it
        first_click = False
        url_entry.delete(0, "end") # delete all the text in the entry



# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

program_name = Label(root, text="YOUTUBE DOWNLOADER",foreground="#6F8D90")
url_entry = Entry(root)
download_video_button = Button(text="DOWNLOAD VIDEO", command=get_video)
download_audio_button = Button(text="DOWNLOAD AUDIO ONLY", command=get_audio)
clear_button = Button(text="CLEAR", command=clear_all)
exit_button = Button(text="QUIT", command=quit)

program_name.config(background="#69F2F0", font=("Sans Serif", 30), anchor=CENTER)
url_entry.config(background="white", foreground="grey", width=59)
clear_button.config(background="#C3B64E", width=56)
download_audio_button.config(background="#298D99", width=26)
download_video_button.config(background='#6D34D9', width=26)
exit_button.config(background="#D9262A", width=56)
url_entry.insert(0, 'Enter Youtube URL...')
url_entry.bind('<FocusIn>', on_entry_click)

program_name.grid(row=0, column=0, columnspan=2)
url_entry.grid(row=1, column=0, columnspan=2, sticky=W)
download_video_button.grid(row=2, column=0)
download_audio_button.grid(row=2, column=1)
clear_button.grid(row=3, column=0, columnspan=2)
exit_button.grid(row=4, column=0, columnspan=2)

root.mainloop()