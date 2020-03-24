# script for Categorize your  files according to extension(search recursively and copy files according to respective files) e.g zip files in .zip folder
import os, sys, shutil
from pathlib import Path
PATHF = Path(sys.argv[1])
print("Before moving file:")
print(os.listdir(PATHF))
for FolderNames, SubFolders, FileNames in os.walk(PATHF):
    for FileName in FileNames:
        p1 = Path(FolderNames, FileName)
        folderEXT = p1.suffix
        pathf = Path(PATHF, folderEXT)#important
        if not os.path.exists(pathf):
            os.makedirs(pathf)
            shutil.copy(str(p1), str(pathf))
        else:
            shutil.copy(str(p1), str(pathf))
print("After moving file:")
print(os.listdir(PATHF))
