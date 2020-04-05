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
    # print("oldFile: " + oldFile)
    newName = randomString(15) 
    newFile = path + "\\" + newName + ".jpg"
    # print("newFile: " + newFile)
    os.rename(oldFile, newFile)

print("Names of files changed!")