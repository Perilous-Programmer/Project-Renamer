import os, time
import sys

path = os.getcwd()+"\\"
#print("path = ", path)
sys.stdout = open(path+"log.txt", "w")


def traverse(dir = ''):
    files = []
    folders = []
    dir = dir + "\\"
    for x in os.listdir(dir):
        if '.' in x: #class 1 and class 2 in files list
            if 'class1' in x:
                files.append(x)
            elif 'class2' in x:
                files.append(x)
        else:
            if 'class1' in x: #class 1 and class 2 in folders list
                folders.append(x)
            elif 'class2' in x:
                folders.append(x)
            try: 
                traverse(dir+x)
            except Exception as err:
                print("plz see ", dir+x)
                print(err)
                files.append(x)
    for file in files: 
        if 'class1' in file: #class 1 and class 2 in rename file names
            newname = file.replace('class1','class1Renamed')
            os.rename(dir+file,dir+newname)
        if 'class2' in file:
            newname = file.replace('class2','class2Renamed')
            os.rename(dir+file,dir+newname)
        print(file)
    for folder in folders: #class 1 and class 2 in rename folder names
        if 'class1' in folder:
            newname = folder.replace('class1','class1Renamed')
            os.rename(dir+folder,dir+newname)
        if 'class2' in folder:
            newname = folder.replace('class2','class2Renamed')
            os.rename(dir+folder,dir+newname)
        print(folder)
    print("path :", dir)
    print("file list :",)
    print(" ",*files, sep = ", "+dir)
    print("folder list :",)
    print(*folders, sep = ", ")
    print("#"*50)

traverse(path+"class1Renamed")

