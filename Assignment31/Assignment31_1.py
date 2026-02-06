#Please follow below rules while designing automation script as
#    Accept input through command line or through file.
#    Display any message in log file instead of console.
#    For separate task define separate function.
#    For robustness handle every expected exception.
#    Perform validations before taking any action.
#    Create user defined modules to store the functionality.
# 1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
#    Usage: Directory FileSearch.py "Demo" ".txt"
#    Demo is name of directory and .txt is the extension that we want to search.

import sys
import os
import time

def CreateLog():

    Logfilename = "FileSearchLog.log"
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


def SearchFiles(dirname, extension, fobj):

    count = 0

    for folder, subfolders, files in os.walk(dirname):

        for fname in files:

            name, ext = os.path.splitext(fname)

            if ext == extension:

                fullpath = os.path.join(folder, fname)

                fobj.write("Found : " + fullpath + "\n")

                count += 1

    fobj.write("Total files found : " + str(count) + "\n")


def main():

    if len(sys.argv) != 3:
        print("Usage: python FileSearch.py <Directory> <Extension>")
        return

    dirname = sys.argv[1]
    extension = sys.argv[2]

    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname, fobj):
            SearchFiles(dirname, extension, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()