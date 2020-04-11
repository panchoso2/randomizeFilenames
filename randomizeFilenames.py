import os
import random
import string
import tkinter
import glob
import numpy as np
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.commondialog import Dialog
import tkinter.filedialog
import tkinter.messagebox
from cv2 import cv2 # I read this on stackoverflow, honestly
from os.path import isfile, join


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
            newName = randomString(25) 
            newFile = path + "\\" + newName + oldFileExtension
            os.rename(oldFile, newFile)
    else:
        tkinter.messagebox.showinfo("Error", "No Directory selected!")
    return True


def compareImages(path):
    if path:
        path = glob.glob(path + "/*.jpg")
        cv_images = []  # store images
        images_names = [] # store images names

        # generate a list of images and a list of their names
        for image in path:
            temp = cv2.imread(image)
            temp_resized = cv2.resize(temp, (2000, 2000))   # resize every image
            cv_images.append(temp_resized)
            images_names.append(image)


        # compare each image with the rest
        removed = []
        for i in range(len(cv_images)):
            # print("Analizing image: " + str(i + 1) + " of " + str(len(cv_images)))
            # duplicateProgress.set(str(i))
            if i not in removed:
                for u in range(i+1, len(cv_images)):
                    result = ssim(cv_images[i], cv_images[u], multichannel = True) # multichannel param allow us to compare colorfull images
                    if result == 1:
                        os.remove(images_names[u])
                        removed.append(u)   # store the deleted image position in list
    else:
        tkinter.messagebox.showinfo("Error", "No Directory selected!")
    return True


# generate window
window = tkinter.Tk()
window.title("Randomize Filenames")
window.geometry("250x250")


# labels
label = Label(window, text="Selected Directory: ")
label.pack()
directory = StringVar()
selectedDirectoryLabel = Label(window, textvariable = directory)
selectedDirectoryLabel.pack()
duplicateProgress = StringVar()
duplicateLabel = Label(window, textvariable = duplicateProgress)
duplicateLabel.pack()

# buttons
buttonSelect = tkinter.Button(window, text = "Select Directory", command = lambda: directoryBrowser(window, directory))
buttonSelect.pack()
buttonChange = tkinter.Button(window, text = "Change Filenames", command = lambda: changeFilenames(directory.get()))
buttonChange.pack()
buttonCompare = tkinter.Button(window, text = "Delete duplicate files", command = lambda: compareImages(directory.get()))
buttonCompare.pack()
window.mainloop()

# labels
# duplicateProgress = StringVar()
# duplicateLabel = Label(window, textvariable = duplicateProgress)
# duplicateLabel.pack()

