import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
import psutil
from email.message import EmailMessage


# ------------------------------------------------
# MAIL
# ------------------------------------------------

def Send_Mail(sender, app_password, receiver, subject, body, attachment):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with open(attachment, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(attachment)
        )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()


# ------------------------------------------------
# LOG FOLDER
# ------------------------------------------------

def CreateLogFolder():
    os.makedirs("Logs", exist_ok=True)


# ------------------------------------------------
# HASH
# ------------------------------------------------

def calculate_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


# ------------------------------------------------
# BACKUP COPY (only changed files)
# ------------------------------------------------

def BackupFiles(Source, Destination):

    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, _, files in os.walk(Source):

        for file in files:

            src = os.path.join(root, file)

            relative = os.path.relpath(src, Source)
            dest = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest), exist_ok=True)

            if (not os.path.exists(dest)) or \
               (calculate_hash(src) != calculate_hash(dest)):

                shutil.copy2(src, dest)
                copied_files.append(relative)

    return copied_files


# ------------------------------------------------
# ZIP CREATION
# ------------------------------------------------

def make_zip(folder):

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    zip_name = os.path.join("Logs", f"Backup_{timestamp}.zip")

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:

        for root, _, files in os.walk(folder):
            for file in files:
                full = os.path.join(root, file)
                relative = os.path.relpath(full, folder)
                z.write(full, relative)

    return zip_name


# ------------------------------------------------
# SYSTEM INFO LOG
# ------------------------------------------------

def CreateLog(file_path, copied_files, zip_name):

    Border = "-" * 50

    with open(file_path, "w") as f:

        f.write(Border+"\n")
        f.write("Marvellous Data Shield System\n")
        f.write("Backup Time : "+time.ctime()+"\n")
        f.write(Border+"\n")

        f.write(f"Files Copied : {len(copied_files)}\n")
        f.write(f"Zip Name : {os.path.basename(zip_name)}\n")

        mem = psutil.virtual_memory()
        f.write(f"RAM Usage : {mem.percent}%\n")

        f.write(Border+"\n")


# ------------------------------------------------
# HISTORY
# ------------------------------------------------

def UpdateHistory(date, count, size):

    with open("BackupHistory.txt", "a") as f:
        f.write(f"{date} | Files:{count} | Size:{size}MB\n")


# ------------------------------------------------
# MAIN BACKUP ENGINE
# ------------------------------------------------

def MarvellousDataShieldStart(Source, email=None):

    CreateLogFolder()

    BackupName = "MarvellousBackup"

    copied = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    log_file = os.path.join("Logs", f"Log_{time.strftime('%Y%m%d_%H%M%S')}.txt")

    CreateLog(log_file, copied, zip_file)

    size = round(os.path.getsize(zip_file)/(1024*1024), 2)

    UpdateHistory(time.ctime(), len(copied), size)

    # send mail if email provided
    if email:
        Send_Mail(
            "nirajpython.test@gmail.com",
            "YOUR_APP_PASSWORD",
            email,
            "Backup Completed",
            f"Files copied: {len(copied)}",
            zip_file
        )


# ------------------------------------------------
# RESTORE
# ------------------------------------------------

def RestoreBackup(zipfile_name, destination):

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zipfile_name, 'r') as z:
        z.extractall(destination)

    print("Restore Completed Successfully")


# ------------------------------------------------
# HISTORY VIEW
# ------------------------------------------------

def ShowHistory():

    if os.path.exists("BackupHistory.txt"):
        with open("BackupHistory.txt") as f:
            print(f.read())


# ------------------------------------------------
# MAIN
# ------------------------------------------------

def main():

    if len(sys.argv) == 4 and sys.argv[1] == "--backup":
        MarvellousDataShieldStart(sys.argv[2], sys.argv[3])

    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])

    elif len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()

    # scheduler mode
    elif len(sys.argv) == 4:
        interval = int(sys.argv[1])
        folder = sys.argv[2]
        email = sys.argv[3]

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart, folder, email)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("Backup     : python script.py --backup SourceDir Email")
        print("Restore    : python script.py --restore ZipFile Dest")
        print("History    : python script.py --history")
        print("Scheduler  : python script.py 5 SourceDir Email")


if __name__ == "__main__":
    main()
