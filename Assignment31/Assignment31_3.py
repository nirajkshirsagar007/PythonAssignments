#3. Design automation script which accept two directory names. 
#    Copy all files from first directory into second directory. Second directory should be created at run time.
#  Usage: Directory Copy.py "Demo" "Temp"
#  Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
import sys
import os
import time
import shutil

def CreateLog():
    timestamp = time.ctime()

    Logfilename = "FileCopyLog%s.log" %(timestamp)

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

def CopyFiles(src,dest,fobj):

    if not os.path.exists(dest):
        os.mkdir(dest)
        fobj.write("Destination directory Created:"+ dest + "\n")

    count = 0

    for FolderName, SubFolderName, FilesName in os.walk(src):

        for fname in FilesName:
            srcPath = os.path.join(FolderName,fname)
            destPath = os.path.join(dest,fname)

            shutil.copy2(srcPath,destPath)

            fobj.write(f"Copied : {srcPath} to {destPath}\n")

            count = count+1
    
    fobj.write("Total files copied: "+str(count)+"\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python FileSearch.py <SourceDir> <DestDir>")
        return

    dirname1 = sys.argv[1]
    dirname2 = sys.argv[2]

    try:
        fobj = CreateLog()

        if ValidateDirectory(dirname1, fobj):
            CopyFiles(dirname1, dirname2, fobj)

        fobj.close()

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()