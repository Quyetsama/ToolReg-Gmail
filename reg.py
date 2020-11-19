from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from multiprocessing import Pool
import time
from time import sleep
from apirentcode import *
from selenium.webdriver.support.ui import Select
from docghitaikhoan import GhiFile
import random
from random import randint
from time import sleep
import subprocess
import threading
def random_sleep(a,b):
    sleep(randint(a,b))
# def Kloadanh():
#     chrome_optionss = webdriver.ChromeOptions()
#     prefs = {
#         "profile.managed_default_content_settings.images": 2
#     }
#     chrome_optionss.add_experimental_option("prefs", prefs)
#     driver = webdriver.Chrome(chrome_options=chrome_optionss)
#     return driver
# def initDriver(filePath):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument(
#         "user-data-dir=" + filePath)
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     return driver

driver = None
run=False
# def reg_gmail():
#     # global driver
#     # if not driver:
#     global run
#     while run:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('excludeSwitches', ['enable-logging'])
#         driver = webdriver.Chrome(r'chromedriver.exe', options=options)
#         try:
#
#             # driver.service.stop()
#             # driver = initDriver(filePath)
#             driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
#             random_sleep(1,5)
#             # name = ['quyet', 'van', 'nguyen', 'long', 'hiep', 'trung', 'hang', 'nga']
#             # sorandom = str(random.randrange(999, 10000))
#             # user = 'tkc' + random.choice(name) + sorandom
#             gmail_user = driver.find_element(By.XPATH, './/*[@id="username"]')
#     # send_keys lần lượt từng chữ random thời gian
#             name = ['quyet', 'van', 'nguyen', 'long', 'hiep', 'trung', 'hang', 'nga']
#             x1 = random.choice(name)
#             x2 = random.choice(name)
#             tg = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#             user = x1 + x2 + str(random.randrange(999, 10000)) + x1
#             for i in user:
#                 time.sleep(random.choice(tg))
#                 gmail_user.send_keys(i)
#             # gmail_user.send_keys(user)
#             random_sleep(1,5)
#             ho = driver.find_element(By.XPATH, './/*[@id="lastName"]')
#             for i1 in x1:
#                 time.sleep(random.choice(tg))
#                 ho.send_keys(i1)
#             random_sleep(1,5)
#             ten = driver.find_element(By.XPATH, './/*[@id="firstName"]')
#             for i2 in x2:
#                 time.sleep(random.choice(tg))
#                 ten.send_keys(i2)
#             random_sleep(1,5)
#             passrandom = ['FVabcd15', 'Kioc33', 'Ufvs64b', 'Pa45igw', 'Yqa86bv', 'Tbjv64a', 'Qbfava28', 'Cbofabso21']
#             passwordd = random.choice(passrandom) + random.choice(passrandom)
#             password = driver.find_element(By.XPATH, './/*[@id="passwd"]/div[1]/div/div[1]/input')
#             for i3 in passwordd:
#                 time.sleep(random.choice(tg))
#                 password.send_keys(i3)
#             random_sleep(1,5)
#             repassword = driver.find_element(By.XPATH, './/*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
#             for i4 in passwordd:
#                 time.sleep(random.choice(tg))
#                 repassword.send_keys(i4)
#             random_sleep(1,5)
#             OK1 = driver.find_element(By.XPATH, './/*[@id="accountDetailsNext"]/span/span')
#             OK1.click()
#             random_sleep(1, 5)
#
#     # order lại so dien thoiaj neu so loi
#             sdt = GetSDT()
#             if len(sdt)==2:
#                 random_sleep(1,5)
#                 sdt_user = driver.find_element(By.XPATH, './/*[@id="phoneNumberId"]')
#                 sdt_user.send_keys(sdt[1])
#                 time.sleep(1)
#                 OK2 = driver.find_element(By.XPATH, './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
#                 OK2.click()
#                 mess = GetMess(sdt[0])
#                 time.sleep(1)
#                 mess_sdt = driver.find_element(By.XPATH, './/*[@id="code"]')
#                 mess_sdt.send_keys(mess)
#                 OK3 = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')
#                 OK3.click()
#                 time.sleep(5)
#
#             else:
#                 sdt2 = GetSDT()
#                 time.sleep(2)
#                 sdt_user = driver.find_element(By.XPATH, './/*[@id="phoneNumberId"]')
#                 sdt_user.send_keys(sdt2[1])
#                 time.sleep(1)
#                 OK2 = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
#                 OK2.click()
#                 mess = GetMess(sdt2[0])
#                 time.sleep(1)
#                 mess_sdt = driver.find_element(By.XPATH, './/*[@id="code"]')
#                 mess_sdt.send_keys(mess)
#                 OK3 = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')
#                 OK3.click()
#                 time.sleep(5)
#
#
#
#             regmail = driver.find_element(By.XPATH, './/*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
#             recovermail = 'vanquyetc2vc1@gmail.com'
#             for j1 in recovermail:
#                 time.sleep(random.choice(tg))
#                 regmail.send_keys(j1)
#             time.sleep(1)
#             day = driver.find_element(By.XPATH,'.//*[@id="day"]')
#             day_keys = '28'
#             for j2 in day_keys:
#                 time.sleep(random.choice(tg))
#                 day.send_keys(j2)
#             time.sleep(1)
#             month = Select(driver.find_element_by_id('month'))
#             month.select_by_value('8')
#             year = driver.find_element(By.XPATH, './/*[@id="year"]')
#             year_keys = '28'
#             for j3 in year_keys:
#                 time.sleep(random.choice(tg))
#                 year.send_keys(j3)
#             time.sleep(1)
#             gioitinh = Select(driver.find_element_by_id('gender'))
#             gioitinh.select_by_value('2')
#             OK4 = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
#             OK4.click()
#             time.sleep(3)
#             toidongy1 = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]')
#             toidongy1.click()
#             # desau = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]')
#             # desau.click()
#             time.sleep(3)
#             driver.execute_script('window.scrollBy(0,2*window.innerHeight)')
#             time.sleep(3)
#             toidongy2 = driver.find_element(By.XPATH,'.//*[@id="termsofserviceNext"]/span/span')
#             toidongy2.click()
#
#             GhiFile(user, passwordd)
#             print('thanh cong')
#             time.sleep(10)
#
#         except:
#             print('Loi khong xac dinh!')
#
#         try:
#             driver.close()
#             driver = None
#         except:
#             pass
#
#
# def Run_Reg(n):
#     global run
#     for i in range(n):
#         run=True
#         browserThread = threading.Thread(target=reg_gmail)
#         browserThread.start()
#
# def close_reg():
#     global driver
#     if driver:
#         driver.quit()
#         driver = None
#     global run
#     run = False
#     subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
#     # subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
#     subprocess.call("taskkill /F /IM chromedriver.exe")




class Register:
    def __init__(self):
        self.driver = None

    def Reg(self):
        global run
        while run:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.driver = webdriver.Chrome(r'chromedriver.exe', options=options)
            try:

                # driver.service.stop()
                # driver = initDriver(filePath)
                self.driver.get(
                    'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
                random_sleep(1, 5)
                # name = ['quyet', 'van', 'nguyen', 'long', 'hiep', 'trung', 'hang', 'nga']
                # sorandom = str(random.randrange(999, 10000))
                # user = 'tkc' + random.choice(name) + sorandom
                gmail_user = self.driver.find_element(By.XPATH, './/*[@id="username"]')
                # send_keys lần lượt từng chữ random thời gian
                name = ['quyet', 'van', 'nguyen', 'long', 'hiep', 'trung', 'hang', 'nga']
                x1 = random.choice(name)
                x2 = random.choice(name)
                tg = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
                user = x1 + x2 + str(random.randrange(999, 10000)) + x1
                for i in user:
                    time.sleep(random.choice(tg))
                    gmail_user.send_keys(i)
                # gmail_user.send_keys(user)
                random_sleep(1, 5)
                ho = self.driver.find_element(By.XPATH, './/*[@id="lastName"]')
                for i1 in x1:
                    time.sleep(random.choice(tg))
                    ho.send_keys(i1)
                random_sleep(1, 5)
                ten = self.driver.find_element(By.XPATH, './/*[@id="firstName"]')
                for i2 in x2:
                    time.sleep(random.choice(tg))
                    ten.send_keys(i2)
                random_sleep(1, 5)
                passrandom = ['FVabcd15', 'Kioc33', 'Ufvs64b', 'Pa45igw', 'Yqa86bv', 'Tbjv64a', 'Qbfava28',
                              'Cbofabso21']
                passwordd = random.choice(passrandom) + random.choice(passrandom)
                password = self.driver.find_element(By.XPATH, './/*[@id="passwd"]/div[1]/div/div[1]/input')
                for i3 in passwordd:
                    time.sleep(random.choice(tg))
                    password.send_keys(i3)
                random_sleep(1, 5)
                repassword = self.driver.find_element(By.XPATH, './/*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
                for i4 in passwordd:
                    time.sleep(random.choice(tg))
                    repassword.send_keys(i4)
                random_sleep(1, 5)
                OK1 = self.driver.find_element(By.XPATH, './/*[@id="accountDetailsNext"]/div/button')
                OK1.click()
                random_sleep(3, 5)

                # order lại so dien thoiaj neu so loi
                print('Dang get so dien thoai')
                sdt = GetSDT()

                if len(sdt) == 2:
                    random_sleep(1, 5)
                    sdt_user = self.driver.find_element(By.XPATH, './/*[@id="phoneNumberId"]')
                    sdt_user.send_keys(sdt[1])
                    time.sleep(1)
                    OK2 = self.driver.find_element(By.XPATH,
                                              './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
                    OK2.click()
                    mess = GetMess(sdt[0])
                    time.sleep(1)
                    mess_sdt = self.driver.find_element(By.XPATH, './/*[@id="code"]')
                    mess_sdt.send_keys(mess)
                    OK3 = self.driver.find_element(By.XPATH,
                                              './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')
                    OK3.click()
                    time.sleep(5)

                else:
                    sdt2 = GetSDT()
                    time.sleep(2)
                    sdt_user = self.driver.find_element(By.XPATH, './/*[@id="phoneNumberId"]')
                    sdt_user.send_keys(sdt2[1])
                    time.sleep(1)
                    OK2 = self.driver.find_element(By.XPATH,
                                              './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
                    OK2.click()
                    mess = GetMess(sdt2[0])
                    time.sleep(1)
                    mess_sdt = self.driver.find_element(By.XPATH, './/*[@id="code"]')
                    mess_sdt.send_keys(mess)
                    OK3 = self.driver.find_element(By.XPATH,
                                              './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button')
                    OK3.click()
                    time.sleep(5)

                regmail = self.driver.find_element(By.XPATH,
                                              './/*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
                recovermail = 'vanquyetc2vc1@gmail.com'
                for j1 in recovermail:
                    time.sleep(random.choice(tg))
                    regmail.send_keys(j1)
                time.sleep(1)
                day = self.driver.find_element(By.XPATH, './/*[@id="day"]')
                day_keys = '28'
                for j2 in day_keys:
                    time.sleep(random.choice(tg))
                    day.send_keys(j2)
                time.sleep(1)
                month = Select(self.driver.find_element_by_id('month'))
                month.select_by_value('8')
                year = self.driver.find_element(By.XPATH, './/*[@id="year"]')
                year_keys = '28'
                for j3 in year_keys:
                    time.sleep(random.choice(tg))
                    year.send_keys(j3)
                time.sleep(1)
                gioitinh = Select(self.driver.find_element_by_id('gender'))
                gioitinh.select_by_value('2')
                OK4 = self.driver.find_element(By.XPATH,
                                          './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
                OK4.click()
                time.sleep(3)
                toidongy1 = self.driver.find_element(By.XPATH,
                                                './/*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]')
                toidongy1.click()
                # desau = driver.find_element(By.XPATH,'.//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]')
                # desau.click()
                time.sleep(3)
                self.driver.execute_script('window.scrollBy(0,2*window.innerHeight)')
                time.sleep(3)
                toidongy2 = self.driver.find_element(By.XPATH, './/*[@id="termsofserviceNext"]/span/span')
                toidongy2.click()

                GhiFile(user, passwordd)
                print('thanh cong')
                time.sleep(10)

            except:
                print('Loi khong xac dinh!')

            try:
                self.driver.close()
                driver = None
            except:
                pass
    def Close(self):
        self.driver.quit()
        # subprocess.call("taskkill /F /IM chromedriver.exe")

# a=Register()
# b=Register()
# c=Register()
# arr = [a,b,c]
a = []

def Run_Reg(n):
    global run
    # x = 0
    # for i in arr:
    #     x+=1
    #     if x==n+1:
    #         break
    #     run = True
    #     threading.Thread(target=i.Reg).start()
    global a
    run = True
    for i in range(n):
        x = Register()
        a.append(x)
        threading.Thread(target=a[i].Reg).start()
def close_reg(n):
    # y = 0
    global run
    run = False
    global a
    # for i in arr:
    #     y+=1
    #     if y==n+1:
    #         break
    #     threading.Thread(target=i.Close).start()
    for i in range(n):
        threading.Thread(target=a[i].Close).start()