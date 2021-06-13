import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from tkinter import filedialog
from PIL import ImageTk,Image
try:
    import pyAesCrypt
except:
    msg.showerror("Status","pyAesCrypt not found \n install using \"pip install pyAesCrypt\" ")
    quit()

def decrypt():
    if(filepath.get()==""):
        msg.showerror("File Status","File Name cannot be empty!!")
    else:
        if(os.path.exists(filepath.get())):
            filepathwaes=filepath.get().split(".aes")[0]
            try:
                pyAesCrypt.decryptFile(filepath.get(),filepathwaes,password.get(),int(buffersize.get()))
                if(delfile.get()=="yes"):
                    os.remove(filepath.get())
                else:
                    pass
                msg.showinfo("File Status","File Decrypted Successfully!!")
                password.set("")
                filepath.set("")
            except ValueError as e:
                msg.showerror("File Status",e)
            except:
                msg.showerror("File Status","an error occured!!")
        else:
            msg.showerror("File Status","File does not exists!!")
    
    
    
def encrypt():
    if(filepath.get()==""):
        msg.showerror("File Status","File Name cannot be empty!!")
    else:
        if(os.path.exists(filepath.get())):
            filepathaes=filepath.get()+".aes"
            try:
                pyAesCrypt.encryptFile(filepath.get(),filepathaes,password.get(),int(buffersize.get()))
                if(delfile.get()=="yes"):
                    os.remove(filepath.get())
                else:
                    pass
                msg.showinfo("File Status","File Encrypted Successfully!!")
                password.set("")
                filepath.set("")
            except:
                msg.showerror("File Status","an error occured!!")
        else:
            msg.showerror("File Status","File does not Exists!!")
    
def browsefile():    
    filepath.set(filedialog.askopenfilename(title="Select File",filetypes=(("all files","*.*"),)))
        
def about():
    global r4
    r4=Toplevel(root)
    r4.title("About this")
    r4.resizable(False,False)
    r4.iconbitmap("lock.ico")
    mf4=ttk.Frame(r4,padding='3 3 12 12')
    mf4.pack(fill="both",expand="yes")
    mf4.rowconfigure(0,weight=1)
    mf4.columnconfigure(0,weight=1)
    l=ttk.Label(mf4,background="#19284B")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="Created By: Hrithik Raj",foreground="white",background="#19284B",font=("Arial Black",16)).grid(row=2,column=0,columnspan=2)
    img=ImageTk.PhotoImage(Image.open("lock.ico"))
    imglbl=ttk.Label(l,background="#19284B",image=img)
    imglbl.photo=img
    imglbl.grid(row=4,column=0,rowspan=3)
    ttk.Label(l,text="File Encrypter",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=4,column=1)
    ttk.Label(l,text="Version : v1.0.0",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=5,column=1)
    ttk.Separator(l,orient="horizontal").grid(row=6,column=0,columnspan=3,sticky="ew")
    ttk.Label(l,text="Email : hrithikraj137@gmail.com",foreground="white",background="#19284B",font=("Calibri",14)).grid(row=7,column=1)
    glbl=ttk.Label(l,text="Github : https://github.com/Cyborg117",foreground="white",background="#19284B",font=("Calibri",14),cursor="hand1")
    glbl.grid(row=9,column=1)
    glbl.bind('<1>',lambda e: webbrowser.open("https://github.com/Cyborg117"))

    for child in l.winfo_children():
        child.grid_configure(pady=10)

def features():
    r5=Toplevel(root)
    r5.title("What's New")
    r5.resizable(False,False)
    r5.iconbitmap("lock.ico")
    mf5=ttk.Frame(r5,padding='3 3 12 12')
    mf5.pack(fill="both",expand="yes")
    mf5.rowconfigure(0,weight=1)
    mf5.columnconfigure(0,weight=1)
    l=ttk.Label(mf5,background="#19284B")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="v1.0.0",foreground="white",background="#19284B",font=("Arial black",16)).grid(row=2,column=0)
    ttk.Separator(l,orient="horizontal").grid(row=3,column=0,columnspan=5,sticky="ew")
    ttk.Label(l,text="1. Encrypt and Decrypt Files",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=5,column=0)
    ttk.Label(l,text="2. Support all File types (*.*) ",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=6,column=0)
    ttk.Label(l,text="3. Encrypt Files Using AES256-CBC Algorithm",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=7,column=0)
    ttk.Label(l,text="4. Use of Password to Encypt or Decrypt Files",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=8,column=0)
    ttk.Label(l,text="5. Set Buffer size of 64Kb to Encrypt/Decrypt \nVery Large Files in 64Kb(default) Chunks\n to not Overload the Memory.",foreground="white",background="#19284B",font=("Calibri",16)).grid(row=9,column=0)

root=Tk()
root.title("File Encrypter v1.0.0")
root.iconbitmap("lock.ico")
root.resizable(False,False)

mainframe=ttk.Frame(root,padding='3 3 12 12')
mainframe.pack(fill="both",expand="yes")
mainframe.rowconfigure(0,weight=1)
mainframe.columnconfigure(0,weight=1)

l=ttk.Label(mainframe,background="#19284B")
l.pack(fill='both',expand='yes')

filepath=StringVar()
buffersize=StringVar()
password=StringVar()
delfile=StringVar()

buffersize.set(int(64*1024))
password.set("12345")

ttk.Label(l,text="File path: ",background="#19284B",foreground="white").grid(row=2,column=2)
e=ttk.Entry(l,textvariable=filepath,width=40)
e.grid(row=2,column=3)
e.focus()
ttk.Button(l,text="Browse",command=browsefile).grid(row=4,column=3)
ttk.Label(l,text="Buffer Size: ",background="#19284B",foreground="white").grid(row=6,column=2)
ttk.Entry(l,textvariable=buffersize).grid(row=6,column=3,sticky='w')
ttk.Label(l,text="Password",background="#19284B",foreground="white").grid(row=8,column=2)
ttk.Entry(l,textvariable=password).grid(row=8,column=3,sticky='w')
ttk.Label(l,text="Delete File after Encrypt/Decrypt",background="#19284B",foreground="white").grid(row=10,column=3,sticky='w')
ttk.Checkbutton(l,variable=delfile,onvalue="yes",offvalue="no",).grid(row=10,column=2)
ttk.Button(l,text="Decrypt",command=decrypt).grid(row=12,column=3)
ttk.Button(l,text="About",command=about).grid(row=14,column=3)
ttk.Button(l,text="Encrypt",command=encrypt).grid(row=12,column=2)
ttk.Button(l,text="Features",command=features).grid(row=14,column=2)

for child in l.winfo_children():
    child.grid_configure(padx=10,pady=10)

root.mainloop()
