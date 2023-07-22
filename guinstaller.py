import subprocess, threading

def install_ctk():
    global root
    ctk_thread = threading.Thread()
    proc = subprocess.Popen("pip install customtkinter", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdoutdata, stderrdata = proc.communicate()
    print(proc.returncode)
    root.destroy()
    if not proc.returncode == 0:
        window1 = Tk()
        frm = ttk.Frame(window1, padding=10)
        frm.grid()
        ttk.Label(frm, text="")
        ttk.Label(frm, text='Installation failed').grid(column=0, row=0)
        ttk.Button(frm, text='Quit', command=window1.destroy).grid(column=0, row=1)

def pip_install_ctk():
    proc = subprocess.Popen("pip install customtkinter", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

try:
    import customtkinter
except ModuleNotFoundError:
    from tkinter import *
    from tkinter import ttk
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text='Hello!').grid(column=0, row=0)
    ttk.Label(frm, text='It looks like a customtkinter needs to be installed.').grid(column=0, row=1)
    ttk.Button(frm, text='Install', command=install_ctk).grid(column=0, row=2)
    ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=3)
    root.mainloop()