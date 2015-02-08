# 7.2) Use more complicated folder structures
import os
import glob
import fnmatch


dropbox_path = "/Users/leo/Dropbox"
real_python = os.path.join(dropbox_path, "projects/real-python")
practice_files = os.path.join(
                dropbox_path,
                "Books/Real Python Course Materials/Chapter 7/Practice files/")
images_dir = os.path.join(practice_files, "images")

# 7.2 Review exercises

print("Display full paths of files and folders in images directory")
files_and_folders = os.listdir(images_dir)
for item in files_and_folders:
    full_filename = os.path.join(practice_files, item)
    print(full_filename)
print()

print("Display full paths of any PNG files in images folder using glob")
possible_png_files = os.path.join(images_dir, "*.png")
for file in glob.glob(possible_png_files):
    print(file)
print()

print("Rename any PNG files in images folder and any subfolders")
for current, subdir, files in os.walk(images_dir):
    for file in files:
        if fnmatch.fnmatch(file, "*.png"):
            old_name = os.path.join(current, file)
            new_name = old_name[0:len(old_name)-4] + ".jpg"
            os.rename(old_name, new_name)
print()

print("Checking that renaming PNG files to JPG files worked")
file1 = os.path.join(images_dir, "png file - not a gif.jpg")
file2 = os.path.join(images_dir, "additional files", "one last image.jpg")
print("Does png file - not a gif.jpg exist?")
print(os.path.exists(file1))
print("Does /additional files/one last image.jpg exist?")
print(os.path.exists(file2))
