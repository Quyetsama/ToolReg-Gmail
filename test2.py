from selenium import webdriver
import time
import threading

class Multiple_Chrome:
    def __init__(self):
        self.driver=None
    def Run(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com.vn/")
        time.sleep(5)
        self.driver.get("https://www.youtube.com/?gl=VN/")
    def Close(self):
        self.driver.quit()



# a=Multiple_Chrome()
# b=Multiple_Chrome()
# c=Multiple_Chrome()
# arr = [a,b,c]
# n = int(input("Nhap so luong: "))
# x = 0
# y = 0
# for i in arr:
#     x+=1
#     if x==n+1:
#         break
#     threading.Thread(target=i.Run).start()
# for i in range(7):
#     time.sleep(1)
#     print(i)
# for i in arr:
#     y+=1
#     if y==n+1:
#         break
#     threading.Thread(target=i.Close).start()


a = []
n = int(input("Nhap so luong: "))
def Run_Run(n):
    global a
    for i in range(n):
        x = Multiple_Chrome()
        a.append(x)
        threading.Thread(target=a[i].Run).start()
#
# def Close_Close(n):
#     global a
#     for i in range(n):
#         threading.Thread(target=a[i].Close).start()
#
Run_Run(n)
# time.sleep(7)
# Close_Close(n)

