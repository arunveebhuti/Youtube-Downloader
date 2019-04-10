import tkinter as tk
from tkinter import *
from pytube import YouTube

def Browse():
    root.destinationDIR= filedialog.askdirectory(initialdir="C:\Python\PyVideo")
    root.destinationText.insert('1', root.destinationDIR)
def Download():
    getVideo = YouTube(root.linkText.get())
    videoStream = getVideo.streams.first()
    videoStream.download(root.destinationDIR)
    messagebox.showinfo("Yo Baby-", "Your video is downloades and saved successfully in \n"+root.destinationDIR)
root = tk.Tk()
root.geometry("565x252")
root.config(background="pink")
label_0 = Label(root, text="     YouTube Downloader     ",width=20,font=("bold", 20),bg="pink")
label_0.place(x=130,y=23)

label_2 = Label(root, text="_________________________________________________",bg="pink")
label_2.place(x=166,y=53)

linkLabel = Label(root, text="ENTER VIDEO LINK : ", bg="white")
linkLabel.place(x=33,y=93)

root.linkText = Entry(root, width=60)
root.linkText.place(x=155,y=93)

destinationLabel = Label(root, text="ENTER DESTINATION : ", bg="white")
destinationLabel.place(x=33,y=133)

root.destinationText = Entry(root, width=38)
root.destinationText.place(x=185,y=133)

brwsButton = Button(root, text="BROWSE", command=Browse, width=8)
brwsButton.place(x=422,y=130)

downloadb = Button(root, text="DOWNLOAD", command=Download, width=33)
downloadb.place(x=177,y=180)
root.mainloop()
