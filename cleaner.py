from tkinter import *
import getpass, os, subprocess, winshell
def temp():
    file_location=r'C:\Users\{user_name}\AppData\Local\Temp'\
        .format(user_name=getpass.getuser())
    pObj=subprocess.Popen('rmdir /S /Q %s' % file_location,
    shell=True, stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
    rTup=pObj.communicate()
    rCod=pObj.returncode
    if rCod==0:
        show_message.config(text='Success: Cleaned Windows Temp Folder')
    else:
        show_message.config(text='Fail: Unable to Clean Temp Folder')

def recycle():
    winshell.recycle_bin().empty(confirm=False,
    show_progress=False, sound=False)
    show_message.config(text='Success: the recycle bin is empty')
window=Tk()
window.title("cleaner")
window.geometry("350x250")

show_message=Label(window, font=("Helvetica", 12))
show_message.grid(row=0, column=0)
show_message.place(anchor=CENTER, relx=.5, rely=.08)

btn=Button(window, text="Delete temp files", font=("Arial", 10), command=temp)
btn.grid(row=1, column=0)
btn.place(relx=.1, rely=.2)

btn2=Button(window, text="Empty recycle bin", font=("Arial", 10), command=recycle)
btn2.grid(row=1, column=1)
btn2.place(relx=.6, rely=.2)

window.mainloop()