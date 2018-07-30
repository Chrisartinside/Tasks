#!/usr/bin/env python3.6

#Tasks 4:

#Write a script that does the following:

#Receives a file_name and line_number as command line parameters.
#Prints the specified line_number from file_name to the screen. The user
#will specify this as you would expect, not using zero as the first line.
#Make sure that you handle the following error cases by presenting the
#user with a useful message:

#The file doesn’t exist.
#The file doesn’t contain the line_number specified (file is too short).

import sys
import os

file_name = sys.argv[1]
file_name_test = file_name.split("/")[-1]
if not os.path.exists(file_name):
    print("The file " + file_name_test + " doesn't exist.")
    exit()

line_number = int(sys.argv[2]) - 1
line_number1 = None

with open(file_name) as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    if len(lines) < line_number + 1:
        print("The file doesn’t contain the line number: " + str(line_number + 1) + " specified (file is too short).")
    else:
        chosen_line = lines[line_number]
        #print(last_line)
        print(chosen_line)
