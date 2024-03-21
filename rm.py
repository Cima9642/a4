import os
import shutil
import sys

#Trash Path
#CHANGE THIS PATH BEFORE SUBMITTING
TRASH_DIR = os.path.expanduser("~/rm_trash")
recursive = False

def increment_filename(file_name):
    
    #Check if the file name exist in trash#
    if not os.path.exists(os.path.join(TRASH_DIR, file_name)):
        return file_name    
    #File name splitter
    name, extension = os.path.splitext(file_name)
    counter = 1
    #While loop to increment counter until a unique name is found
    while True:
        new_filename = name + "-" + str(counter) + extension
        if not os.path.exists(os.path.join(TRASH_DIR, new_filename)):
            return new_filename
        counter += 1

def move_to_trash(path):
    #Does the path point to a file?
    file_name = os.path.basename(path)
    new_filename = increment_filename(file_name)
    
    if os.path.isfile(path):
        #Increase file name and move to trash
        shutil.move(path, os.path.join(TRASH_DIR, new_filename))
    #Check if path points to a directory
    elif os.path.isdir(file_name):
        #Error Printer and change directories  
        shutil.move(file_name, os.path.join(TRASH_DIR, new_filename))
    #Satisfies no conditions, print    
    else:
        print("rm.py: cannot remove " + path  + ": No such file or directory", file=sys.stderr) 

def main():
    #Trash doesn't exist? Make one
    if not os.path.exists(TRASH_DIR):
        os.makedirs(TRASH_DIR)

    #Recursion Stuff
    recursive = False
    args = sys.argv[1:]
    if "-r" in args:
        recursive = True
        args.remove("-r")    
        
   #Trash arg mover
    for path in args:
        if recursive:
            move_to_trash(path)
        elif os.path.isfile(path):
            move_to_trash(path)
        else:
            print("rm.py: cannot remove " + path + ": Is a directory", file=sys.stderr) 
            
if __name__ == "__main__":
    main()