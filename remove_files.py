# Assignment 7.2: Use pattern matching to delete files
import os
import fnmatch


ch7_files = "/Users/leo/Dropbox/Books/Real Python Course Materials/Chapter 7"
little_pics = os.path.join(ch7_files, "Practice files", "little pics")


for top, subs, files in os.walk(little_pics):
    for file in files:
        if fnmatch.fnmatch(file, "*.jpg"):
            full_name = os.path.join(top, file)
            print(full_name)
            
            if os.path.getsize(full_name) < 2000:
                print("Deleting {}...".format(full_name))
                os.remove(full_name)

