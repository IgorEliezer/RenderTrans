#!/usr/bin/env python

"""render.py: a small python app that renders multiple blender files. Single file."""

__author__ = 'Igor Eliezer'
__copyright__ = "Copyright 2015, Igor Eliezer ME"
__date__ = '2015/01/02'
__status__ = "Prototype"

import glob
import os

print("\nRenderTrans: A Python application.")
print("Created by: " + __author__ + " (www.igoreliezer.com)")
print("Creation date: " + __date__)
print("Initializing...")
input("\nHit ENTER to proceed: ")

# Variables
path_root = os.getcwd()
path_in = os.path.join(path_root, "test") # leave "" to work locally
path_out = os.path.join(path_in, "render")
path_blender = "cd \"C:\Program Files\Blender Foundation\Blender\""
file_type_in = "*.blend"
# file_type_out = "*.png" # not necessary a.t.m.

# Input directory
print("-- Looking for blender files in: " + path_in)

# Output directory
if (os.path.isdir(path_out)):
    print("-- The 'render' directory was found in " + path_in + ".")
else:
    print("-- The 'render' directory was NOT found in " + path_in + "!")
    input("-- Hit ENTER to create it: ")
    os.makedirs(path_out)
    print("-- Will now output in: " + path_out)

# Filter
file_filter = os.path.join(path_in, file_type_in)
print("\n-- Using file filter: " + file_filter)

# List files in directory
files = glob.glob(file_filter)
print("-- {0} blend files were found in {1}".format(str(len(files)), path_in))
input("-- Hit ENTER to create the batch file: ")

# Create a file
file_batch = os.path.join(path_in, "script.txt")
print("\n-- Creating... (it may take a while)")

# Write "blender -b file.blend -o //file -F PNG -x 1 -f 1"
f = open(file_batch, 'w')
f.write(path_blender + "\n")
for file in files:
    file_name_ext = os.path.split(file)[1]
    file_name = os.path.splitext(file_name_ext)[0] #remove file extension
    line = "blender -b " + file + " -o " + "//render\\" + file_name + " -F PNG -x 1 -f 1"
    f.write(line + "\n")
    print("--> Witting: " + line)
f.write("PAUSE")
f.close()

#Check if successful
if (os.path.isfile(file_batch)):
    print("\n-- The batch " + file_batch + " was created.")
else:
    print("\n-- The batch " + file_batch + " was NOT created.")

# Done
print("Done!")

# TODO: create modules for log and other tasks
# Read the damn config
def read_config(file):
    """
This reads a config file

    """
    with open(file) as f:
        for line in f:
            pass


# Remove 0001.png from PNG
def trim_file_name(file):
    pass

# Log in file
def log_it(bool):
    file = "log.txt"
    str_header = """@Echo on
                    SET LOGFILE=Render.log
                    call :Logit >> %LOGFILE%
                    exit /b 0

                    :Logit"""
