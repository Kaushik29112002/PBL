# PBL
This code is for the organizing the files automatically

Firstly, we need to import the required modules i.e. import OS and import shutil

IMPORT OS

The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.

IMPORT SHUTIL
The Shutil module in Python provides many functions of high-level operations on files and collections of files. It also comes under Python's standard utility modules. This module helps in automating the process of copying and removing of files and directories.
Import OS & Import Shutil are in-built modules and don't need to install them.

I have created variable called path which takes the path from user and stores directory path which we wants to organize.
 and then created Variable called FILES which consists of list of files.
using
os.listdir() :
This method returns a list of all the files and folders present inside the specified directory. If no directory is specified then the list of files and folders inside the CURRENT WORKING DIRECTORY is returned.
Now for loop condition

Using for loop we traverse through every files from FILES.

If files ends with particular extension
And check whether the folder for this extension exists or not using OS.PATH.EXISTS().

Here os.path.exists() method in Python is used to check whether the specified path exists or not.

if the folder for this extension is not exists then creating directory using os.makedirs() method.

This method creates a directory recursively. It means that while creating a leaf directory if any of the intermediate level directories specified in the path is missing then the method creates them all.

After creating directory using
shutil.move() method,it Recursively moves a file or source to another destination and returns the destination.
OR
If the folder for this extension is already exists then it directly moves using SHUTIL.MOVES().

Apply this for multiple extensions like .txt, .py, .jpeg, .mp4.
