#  2. Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extention.
#     Usage: Directory Rename.py "Demo" ".txt" ".doc"
#     Demo is name of directory and .txt is the extension that we want to search and rename with.doc.
#     After execution this script each .txt file gets renamed as .doc.   


import sys
import os
import time

def CreateLog():
    timestamp = time.ctime()

    Logfilename = "FileRenameLog%s.log" %(timestamp)

    Logfilename = Logfilename.replace(" ","_")
    Logfilename = Logfilename.replace(":","_")

    
    fobj = open(Logfilename, "a")

    fobj.write("\n------------------------------------\n")
    fobj.write("Log created at : " + time.ctime() + "\n")

    return fobj

def ValidateDirectory(dirname, fobj):

    if not os.path.exists(dirname):
        fobj.write("ERROR : Directory does not exist\n")
        return False

    if not os.path.isdir(dirname):
        fobj.write("ERROR : Path is not directory\n")
        return False

    return True


def RenameFiles(dirname, extension1,extension2, fobj):

    count = 0

    for folder, subfolders, files in os.walk(dirname):
 
        for fname in files:

            name, ext = os.path.splitext(fname)

            if ext == extension1:

                Oldpath = os.path.join(folder, fname)
                newName = name + extension2
                newPath = os.path.join(folder,newName)

                os.rename(Oldpath,newPath)
                fobj.write(f"Renamed: {Oldpath} to {newPath}\n")
                count += 1

    fobj.write("Total files renamed : " + str(count) + "\n")


def main():

    if len(sys.argv) != 4:
        print("Usage: python FileSearch.py <Directory> <Extension>")
        return

    dirname = sys.argv[1]
    extension1 = sys.argv[2]
    extension2 = sys.argv[3]

    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname, fobj):
            RenameFiles(dirname, extension1,extension2, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()