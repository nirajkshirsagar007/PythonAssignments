#Please follow below rules while designing automation script as
#  Accept input through command line or through file.
#  Display any message in log file instead of console.
#  For separate task define separate function.
#  For robustness handle every expected exception.
#  Perform validations before taking any action.
#  Create user defined modules to store the functionality.

#4. Design automation script which accept directory name and delete all duplicate files from that directory. 
#   Write names of duplicate files from that directory into log file named as Log.txt. 
#   Log.txt file should be created into current directory. Display execution time required for the script.
#   Usage: Directory DusplicateRemoval.py "Demo"
#   Demo is name of directory.

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
    for FolderName, SubFolderName, FileName in os.walk(directory):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
            
    return Duplicate

def DeleteDuplicate(directory, fobj):

    MyDict = CheckDuplicate(directory, fobj)

    Cnt = 0

    for value in MyDict.values():

        if len(value) > 1:

            for subvalue in value[1:]:
                try:
                    os.remove(subvalue)
                    fobj.write("Deleted File : " + subvalue + "\n")
                    Cnt += 1
                except Exception as e:
                    fobj.write("Error deleting " + subvalue + " : " + str(e) + "\n")

    fobj.write("Total Deleted Files: " + str(Cnt) + "\n")
    
def main():

    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python FileSearch.py <SourceDir> <DestDir>")
        return

    dirname1 = sys.argv[1]
    
    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname1, fobj):
            DeleteDuplicate(dirname1, fobj)


    except Exception as e:
        print("Unexpected error:", e)

    finally:
        end_time = time.time()

        fobj.write("\nExecution Time : %.2f seconds\n" % (end_time - start_time))
        fobj.close()

if __name__ == "__main__":
    main()