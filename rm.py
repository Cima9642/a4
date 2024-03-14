import os
import sys
import shutil



def apender(directory):
    files = os.listdir(directory)
    counter = {}
    
    for file in files:
        name, extension = os.path.splitext(file)
        
        if "-" in name[-2:]:
            base_name, counter = name.rsplit('-', 1)
            if count.isdigit():
                count = int(count)
            else:
                count = 1
                base_name = name
        else:
            count = 0
            base_name = name
        
        #Increment counter for the base name
        counter[base_name] = counter.get(base_name, count) + 1
        
        #New file formatter
        name_after = "{}-{}{}".format(base_name, counter[base_name], extension)
        
        #File path builder
        prev_path = os.path.join(directory, file)
        new_path = os.path.join(directory, name_after)
        
        #Renaminator
        shutil.move(prev_path, new_path)
        #TESTER DELETE AFTER USE, FIGURE OUT HOW TO EXACTLY RUN IT FUCKER
        #print("Renamed file '{}' to '{}'".format(file, name_after)) 
    path_getter = sys.argv[1:]
    
    #FunkyTown
    des_dir = os.path.expanduser("~/rm_trash")
    
    
        
        
        
        
        
        
        
        