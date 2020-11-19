from reg import *
from tkinter import *
import threading
from tkinter.ttk import *
import tkinter
from apirentcode import API_get, So_Du


def KT_sodu():
    n1 = str(stringAPIKeys.get())
    threading.Thread(target=API_get, args=(n1,)).start()
    content = "Số dư: " + str(So_Du())
    label3.config(text = content)

root=Tk()
stringAPIKeys=StringVar()
stringdaluong=Variable()
soacc=Variable()

def Run():
    n = int(combo.get())
    n1 = str(stringAPIKeys.get())
    threading.Thread(target=API_get, args=(n1,)).start()
    threading.Thread(target=Run_Reg, args=(n,)).start()

def Close():
    n = int(combo.get())
    threading.Thread(target=close_reg, args=(n,)).start()

def Thread_Sodu():
    threading.Thread(target=KT_sodu).start()


root.title('Tool Regmail')
root.resizable(height=True,width=True )
root.minsize(height= 350,width= 350)

label_main = tkinter.Label(root,text='Auto Q',fg='blue',font=('toahama',16),justify=CENTER)
label_main.pack(pady=5)
# listbox=Listbox(root,width=58)      #listbox phải khai báo 2 dòng
# listbox.grid(row=1,columnspan=2)

label1 = tkinter.Label(root,text='APIKeys:',fg='red')
label1.pack(pady=5)
entry1 = Entry(root,width=30,textvariable=stringAPIKeys)
entry1.pack(pady=5)
btn = Button(root, text="Kiểm tra số dư", command=Thread_Sodu)
btn.pack()
label3 = Label(root,text='số dư: 0')
label3.pack(pady=5)
label2 = tkinter.Label(root, text='Số luồng:',fg='red')
label2.pack(pady=10)
combo = Combobox(root)
combo['value'] = (1,2,3)
combo.current(0)
combo.pack(pady=5)

button = Button(root,text='Bắt đầu',command=Run)
button.pack(pady=15)

button = Button(root,text='Dừng',command=Close)
button.pack(pady=5)


root.mainloop()

