import subprocess, threading
from tkinter import *
from tkinter import ttk
def install_ctk():
    global root, stdoutdata, window1
    ctk_thread = threading.Thread()
    proc = subprocess.Popen("pip install customtkinter", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdoutdata, stderrdata = proc.communicate()
    root.destroy()
    if not proc.returncode == 0:
        window1 = Tk()
        frm = ttk.Frame(window1, padding=10)
        frm.grid()
        ttk.Label(frm, text="")
        ttk.Label(frm, text='Installation failed').grid(column=0, row=0)
        ttk.Button(frm, text='Quit', command=window1.destroy).grid(column=0, row=1)
        ttk.Button(frm, text='Show Error Message', command=show_error).grid(column=1, row=1)
#        ttk.Button(frm, text="Try again, but with pipx this time", command=pipx_install_ctk).grid(column=0, row=2)
    elif proc.returncode == 0:
        window1 = Tk()
        frm = ttk.Frame(window1, padding=10)
        frm.grid()
        ttk.Label(frm, text="")
        ttk.Label(frm, text='Installation was a success!').grid(column=0, row=0)
        ttk.Button(frm, text='Quit', command=window1.destroy).grid(column=0, row=1)
def show_error():
    global window2
    window1.destroy()
    window2 = Tk()
    frm = ttk.Frame(window2, padding=10)
    frm.grid()
    ttk.Label(frm, text=stdoutdata).grid(column=0, row=0)
    ttk.Button(frm, text='Quit', command=window1.destroy).grid(column=0, row=26)

def pipx_install_ctk():
    proc = subprocess.Popen("pipx install customtkinter", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdoutdata, stderrdata = proc.communicate()
    window1.destroy()
    if not proc.returncode == 0:
        window3 = Tk()
        frm = ttk.Frame(window3, padding=10)
        frm.grid()
        ttk.Label(frm, text="")
        ttk.Label(frm, text='Installation failed').grid(column=0, row=0)
        ttk.Button(frm, text='Quit', command=window3.destroy).grid(column=0, row=1)

def main():
    global root
    try:
        import customtkinter
    except ModuleNotFoundError:
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text='Hello!').grid(column=0, row=0)
        ttk.Label(frm, text='It looks like a customtkinter needs to be installed.').grid(column=0, row=1)
        ttk.Button(frm, text='Install', command=install_ctk).grid(column=0, row=2)
        ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=3)
        root.mainloop()

main()