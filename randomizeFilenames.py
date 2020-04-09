# this script uses python 2.7

import os
import random
import string
import tkinter
from tkinter import *
from tkinter.commondialog import Dialog
import tkinter.filedialog
import tkinter.messagebox

# generate random name function
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def directoryBrowser(window, directory):
    path = tkinter.filedialog.askdirectory(initialdir="/",title='Please select a directory')
    directory.set(path)
    return path

def changeFilenames(path):

    if path:
        files = os.listdir(path)
        for i in files:
            oldFile = path + "\\" + i
            oldFileExtension = os.path.splitext(oldFile)[1] # get file extension
            newName = randomString(20) 
            newFile = path + "\\" + newName + oldFileExtension
            os.rename(oldFile, newFile)
    else:
        tkinter.messagebox.showinfo("Error", "No Directory selected!")
    return TRUE



# generate window
window = tkinter.Tk()
window.title("Randomize Filenames")
window.geometry("250x250")



# labels
label = Label(window, text="Selected Directory: ")
label.pack()
directory = StringVar()
selectedDirectoryLabel = Label(window, textvariable=directory)
selectedDirectoryLabel.pack()


# buttons
buttonSelect = tkinter.Button(window, text="Select Directory", command=lambda: directoryBrowser(window, directory))
buttonSelect.pack()
buttonStart = tkinter.Button(window, text="Change Filenames", command=lambda: changeFilenames(directory.get()))
buttonStart.pack()


window.mainloop()