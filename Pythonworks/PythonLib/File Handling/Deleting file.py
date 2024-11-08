import os
#os.remove("abc.txt")

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("file not found")

os.rmdir("New Folder")