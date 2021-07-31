import sys
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# function to create necessary widgets
def AppWidgets():
    
	link_label = Label(root, text="Paste Link :")
	link_label.grid(row=1, column=0, pady=5, padx=5)

	linkText = Entry(root, width=55, textvariable=yt_Link)
	linkText.grid(row=2, column=1, pady=5, padx=5, columnspan = 2)

	destination_label = Label(root, text="Storage Location :",)
	destination_label.grid(row=3, column=0, pady=5, padx=5)

	destinationText = Entry(root, width=40, textvariable=download_Path)
	destinationText.grid(row=4, column=1, pady=5, padx=5)

	dir_button = Button(root, text="Choose Directory", command=ChooseDir, width=15, bg="#DCB2E6")
	dir_button.grid(row=4, column=0, pady=1, padx=1)

	download_button = Button(root, text="Download", command=Download, width=20, bg="#DCB2E6")
	download_button.grid(row=6, column=1, pady=3, padx=3)

# Defining a function to select the storage location for the downloaded video
def ChooseDir():
	# reading the storage location chosen by the user
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")

	# Displaying the directory in the textbox
	download_Path.set(download_Directory)

# Defining a function to download the video
def Download():
	
	# prompting the user to provide a YouTube link
	Youtube_link = yt_Link.get()
	
	# selecting a location for the download
	download_Folder = download_Path.get()

	# creating an object of the YouTube class
	getVideo = YouTube(Youtube_link)

	# getting the available streams of the video and selecting the first one
	videoStream = getVideo.streams.first()

	# Downloading the video to chosen directory
	videoStream.download(download_Folder)

	# Displaying the message
	messagebox.showinfo("Request successful!", "Video downloaded and saves in the directory: \n" + download_Folder)

# Creating object of tk class
root = tk.Tk()

# title and size of the application window:
root.geometry("750x200")
root.title("YOUTUBE DOWNLOADER APP")
root.resizable(True, True)

# declaring the variables: 
yt_Link = StringVar()
download_Path = StringVar()

# Calling the Widgets() function
AppWidgets()

# running the downloader using an infinite loop
root.mainloop()
