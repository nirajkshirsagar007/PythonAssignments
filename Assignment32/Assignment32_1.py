#Please follow below rules while designing automation script as
#  Accept input through command line or through file.
#  Display any message in log file instead of console.
#  For separate task define separate function.
#  For robustness handle every expected exception.
#  Perform validations before taking any action.
#  Create user defined modules to store the functionality.

#1. Design automation script which accept directory name and display checksum of all files.
#  Usage: DirectoryChecksum.py "Demo"
#  Demo is name of directory.

import sys
import os
import time
import hashlib

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName,"rb")

        hobj = hashlib.md5()
        Buffer = fobj.read(1024)
        while(len(Buffer)>0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()

        return hobj.hexdigest()
    except Exception:
        return "Error"

def CreateLog():
    timestamp = time.ctime()

    Logfilename = "DirectoryChecksumLog_%s.log" %(timestamp)

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

def DisplayChecksum(directory,fobj):

    count = 0

    for FolderName, subFolderName, FileName in os.walk(directory):
        for fName in FileName:
            FullPath = os.path.join(FolderName,fName)
            checksum = CalculateChecksum(FullPath)

            fobj.write(f"{FullPath} -->CheckSum: {checksum}\n")
            count = count+1

    fobj.write("Total files processed : " + str(count) + "\n")

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python FileSearch.py <SourceDir> <DestDir>")
        return

    dirname1 = sys.argv[1]
    
    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname1, fobj):
            DisplayChecksum(dirname1, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()