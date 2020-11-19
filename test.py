# def abc():
#     s = 'quyetdaica'
#     a = [s]
#     print(a[0])
#     s1= 'tao la quyet'
#     a.append(s1)
#     print(a)
#     return a
# qc=abc()
# print(len(abc()))
# if len(abc())==2:
#     print('a')
# else:
#     print('b')
# print(qc[0])


# s= 'G-189020 là mã xác minh Google của bạn.'
# x = s.find('-')
# print(s[x+1:])
# x2 = s.find(' ')
# ma = s[x+1:x2]
# print(type(ma))


# for i in range(10):
#     driver.execute_script('window.scrollBy(0,0.7*window.innerHeight)')
#     time.sleep(2)
# time.sleep(5)


# try:
#     n=int(input())
#     print(n)
# except:
#     print('loi')



# get ip:port
# import requests
# from selenium import webdriver
# url = "https://proxypage1.p.rapidapi.com/v1/tier1"
#
# querystring = {"limit":"100","country":"US","type":"HTTP"}
#
# headers = {
#     'x-rapidapi-host': "proxypage1.p.rapidapi.com",
#     'x-rapidapi-key': "7da5185f9amsha01c484dc882bdep1f67fdjsn4e2148eb6d61",
#     'content-type': "application/x-www-form-urlencoded"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# a= response.json()
# print(a[0])
# x = a[0]
# print(x['ip'])
# print(x['port'])
# # change ip
# s1 = x['ip']
# s2 = str(x['port'])
# haicham = ':'
# s = s1 + haicham + s2
# PROXY = s # IP:PORT or HOST:PORT
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
#
# chrome = webdriver.Chrome(chrome_options=chrome_options)
# chrome.get("http://whatismyipaddress.com")

# from random import randint
# from time import sleep
# def randomm_sleep(a,b):
#     sleep(randint(a,b))
# randomm_sleep(1,5)
# print('qc')


# import requests
#
# url = "https://proxy-orbit1.p.rapidapi.com/v1/"
#
# headers = {
#     'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com",
#     'x-rapidapi-key': "7da5185f9amsha01c484dc882bdep1f67fdjsn4e2148eb6d61"
#     }
#
# respons = requests.request("GET", url, headers=headers)
# x= respons.json()
# print(respons.json())
# print(x["curl"])
#
# s = x["curl"]
# x1 = s.rfind('/')
# ipport = s[x1 + 1:]
# print(ipport)
#
#
#
# proxies={
#     'https':ipport,
#     'http':ipport
# }
#
# url = 'http://httpbin.org/ip'
#
# resp = requests.get(url,proxies=proxies)
# print(resp.json())
#
# from selenium import webdriver
#
# PROXY = ipport # IP:PORT or HOST:PORT
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
#
# chrome = webdriver.Chrome(chrome_options=chrome_options)
# chrome.get("http://whatismyipaddress.com")



# from daluong import *
# from multiprocessing import Pool
# from tkinter import *
# import tkinter
# from tkinter.ttk import *
#
# window = Tk()
# window.title('QKC')
# window.geometry('500x300')
#
# # thêm label
# lbl = tkinter.Label(window, text='Hello anh em', fg='red', font=('Arial', 50))
# lbl.grid(column=0, row=0)
#
# # thêm texbox
# txt = Entry(window, width=50)
# txt.grid(column=0, row=1)
#
# def handleButton():
#     lbl.config(text='Hi,' + txt.get())
#     return
#
# def pool_handler(x):
#     p = Pool(x)
#     # kq = p.map_async(reg_gmail, ('chrome1', 'chrome2'))
#     kq = p.map_async(reg_gmail, 'chrome1')
#
# # thêm button
# btnHello = Button(window, text='Say Hello',command=handleButton)
# btnHello.grid(column=1, row=1)
#
#
# # thêm combobox
# combo = Combobox(window)
# combo['value'] = ('1', '2', '3', '4', '5')
# # mặc định là 1 luồng
# combo.current(0)
# combo.grid(column=0, row=2)
#
# def Run():
#     pool_handler(combo.get())
#     lbl.config(text='Hi,' + combo.get())
#     return
# # thêm button
# btnHello1 = Button(window, text='Run',command=Run)
# btnHello1.grid(column=1, row=2)
#
# window.mainloop()
#
#
# if __name__ == '__main__':
#     pool_handler(x)
# import random
# import time
# passrandom = ['FVabcd15', 'Kioc33', 'Ufvs64b', 'Pa45igw', 'Yqa86bv', 'Tbjv64a', 'Qbfava28', 'Cbofabso21']
# passwordd = random.choice(passrandom) + random.choice(passrandom)
# print(passwordd)
# tg = [0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
# # x=random.choice(name)+random.choice(name)+str(random.randrange(999, 10000))
# for i in passwordd:
#     time.sleep(random.choice(tg))
#     print(i)


# from tkinter import *
# import time
# from random import randint
# import threading
# import requests
# root = Tk()
# def run():
#     for i in range(1,6):
#         time.sleep(1)
#         print(i)
#     label.config(text='5 seconds is up!')
# def runbutton():
#     threading.Thread(target=run).start()
# def rando():
#     random_label.config(text=f'Random number: {randint(1,100)}')
#
# label = Label(root, text="quyet van")
# label.pack(pady=20)
# button1 = Button(root, text='5second', command=runbutton)
# button1.pack(pady=20)
# button2 = Button(root, text='random', command=rando)
# button2.pack(pady=20)
#
# random_label = Label(root, text='')
# random_label.pack(pady=20)
#
#
#
# root.mainloop()

# response = requests.get('https://api.rentcode.net/api/v2/balance?apiKey=vivvTm7TgEYIJFV7I9tQvnvLsDtT9WQ8k51eeBPZAiQv')
# x = response.json()
# print(x['results'])

# from tkinter import *
# from selenium import webdriver
# import threading
#
# driver = None
# def on_open():
#     global driver
#     if not driver:
#         driver = webdriver.Chrome()
#         url = e.get()
#         driver.get(url)
#
# def on_close():
#     global driver
#     if driver:
#         driver.close()
#         driver = None
#
# def Run():
#     threading.Thread(target=on_open).start()
#
# root  = Tk()
# e = Entry(root)
# e.pack()
# e.insert('end', 'https://stackoverflow.com')
# b = Button(root, text='Selenium Open', command=Run)
# b.pack()
# b = Button(root, text='Selenium Close', command=on_close)
# b.pack()
# root.mainloop()
from selenium import webdriver
import multiprocessing
import time
from reg import *
import subprocess
driver = None


# def Close():
#     global driver
#     if driver:
#         try:
#             driver.quit()
#         except:
#             print('khong the quit')
#     subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
#     subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
#     driver = 1
#     print(driver, 'dung cc')
# def Chrome():
#     global driver
#     while True:
#
#         driver = None
#         if driver == None:
#             try:
#                 driver = webdriver.Chrome()
#                 driver.get('https://www.google.com.vn/')
#                 # time.sleep(10)
#                 for i in range(10):
#                     time.sleep(1)
#                     print(i)
#                 try:
#                     print('da quit')
#                     driver.quit()
#                 except:
#                     print('da except quit')
#                 # try:
#                 #     print('driver=None')
#                 #     driver = None
#                 # except:
#                 #     print('da except driver=None')
#             except:
#                 driver = 1
#                 print("loi khong XD")
#                 print(driver)
#         print(driver)
#         if driver == 1:
#             print('Da dung')
#             break
#
#
# def Chrome1():
#     # global driver
#     # if driver == None:
#     while True:
#         global driver
#         print('deoo dung ak')
#         print(driver, 'deoo dung ak')
#         if driver == 1:
#             print(driver, 'driver dung cai tao xem nao')
#             print('dung me may di ditt con me may')
#             break
#         driver = None
#         Chrome()
#
# def Run(n):
#     global driver
#     processes = []
#     for _ in range(n):
#         p = multiprocessing.Process(target=Chrome)
#         p.start()
#         processes.append(p)
#     for process in processes:
#         process.join()

# def Global_driver():
#     global driver
#     return driver
run=False
def Chrome():
    # global driver
    # if not driver:
    global run
    while run:
        # global driver
        # if driver != 1:
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.google.com.vn/')
            # time.sleep(10)
            for i in range(10):
                time.sleep(1)
                print(i)
            # try:
            #     print('driver=None')
            #     driver = None
            # except:
            #     print('da except driver=None')
        except:
            print("loi khong XD")
        try:
            driver.close()
            driver = None
        except:
            pass
        # if driver.quit()==True:
        #     break
        # # else:
        # #     break
# def Chrome1():
#     # global driver
#     # if driver == None:
#     while True:
#
#         x = Chrome()
#         global driver
#         if driver == None:
#             print('da break')
#             break


def Run(n):
    global run
    for i in range(n):
        run=True
        browserThread = threading.Thread(target=Chrome)
        browserThread.start()
# def Run(n):
#     global run
#     processes = []
#     for _ in range(n):
#         run = True
#         p = multiprocessing.Process(target=Chrome)
#         p.start()
#         processes.append(p)
#     for process in processes:
#         process.join()



# import subprocess
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# link = 'https://google.com'
# driver.get(link)
# # s = driver.page_source
# # print((s.encode("utf-8")))
# time.sleep(5)
# subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
# subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")

def Close():
    global driver
    global run
    # if driver:
    #     driver.quit()
    driver = 1
    run=False
    subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
    subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")



