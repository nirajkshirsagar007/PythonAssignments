#Please follow below rules while designing automation script as
#  Accept input through command line or through file.
#  Display any message in log file instead of console.
#  For separate task define separate function.
#  For robustness handle every expected exception.
#  Perform validations before taking any action.
#  Create user defined modules to store the functionality.

#2. Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory.
#    Usage: Directory Dusplicate.py "Demo"
#    Demo is name of directory.

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

    Logfilename = "Log_%s.txt" %(timestamp)

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

def CheckDuplicate(directory,fobj):

    total_files = 0
    Duplicate = {}

    for FolderName, subFolderName, FileName in os.walk(directory):
        for fName in FileName:
            FullPath = os.path.join(FolderName,fName)
            Checksum = CalculateChecksum(FullPath)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(FullPath)
            else:
                Duplicate[Checksum] = [FullPath]
            
            total_files = total_files+1

    duplicate_count = 0

    for key, filelist in Duplicate.items():

        if len(filelist) > 1:

            fobj.write("\nDuplicate files:\n")

            for file in filelist:
                fobj.write(file + "\n")

            duplicate_count += len(filelist)


    fobj.write("\nTotal files scanned : " + str(total_files) + "\n")
    fobj.write("Total duplicate files : " + str(duplicate_count) + "\n")

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python FileSearch.py <SourceDir> <DestDir>")
        return

    dirname1 = sys.argv[1]
    
    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname1, fobj):
            CheckDuplicate(dirname1, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()