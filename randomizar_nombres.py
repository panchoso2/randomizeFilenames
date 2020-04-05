import os
import random
import string

# generate random name
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print("Enter dir's name: ")
path = raw_input()

# list of files names
files = os.listdir(path)

# change name of every file in path
for i in files:
    oldFile = path + "\\" + i
    oldFileExtension = os.path.splitext(oldFile)[1] # get file extension
    newName = randomString(15) 
    newFile = path + "\\" + newName + oldFileExtension
    os.rename(oldFile, newFile)

print("Filenames changed!")