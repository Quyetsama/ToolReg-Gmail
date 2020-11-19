from tkinter import *
import tkinter
from tkinter.ttk import *
from test import *
import threading

if __name__ == "__main__":
    window = Tk()
    def RunChrome():
        n = int(combo.get())
        Run(n)

    def Thread_Run():
        threading.Thread(target=RunChrome).start()

    def Thread_Close():
        threading.Thread(target=Close).start()
    window.title('QKC')
    window.geometry('500x350')
    lbl = tkinter.Label(window, text='Hello anh em', fg='red', font=('Arial', 50))
    lbl.pack(pady=20)

    lbl = tkinter.Label(window, text='Số luồng')
    lbl.pack(pady=10)
    combo = Combobox(window)
    combo['value'] = (1,2,3)
    combo.current(0)
    combo.pack(pady=20)

    btn = Button(window, text='Run', command=Thread_Run)
    btn.pack(pady=20)
    btn = Button(window, text='Close', command=Thread_Close)
    btn.pack(pady=20)

    window.mainloop()
