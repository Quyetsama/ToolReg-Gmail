# n=1
# def KC():
#     global n
#     while True:
#
#         print(n)
#         n = n+1
#         if n==5:
#             break
# KC()

def Close():
    global driver
    if driver:
        driver.quit()
        driver = None
    subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
    subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")

def Chrome():
    # global driver
    # if not driver:
    while True:
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
            driver = 1
            print("loi khong XD")
            print(driver)

        try:
            driver.close()
            driver = None
        except:
            pass

def Chrome1():
    # global driver
    # if driver == None:
    while True:

        x = Chrome()
        global driver
        if driver == None:
            print('da break')
            break

# def Run(n):
#     global driver
#     processes = []
#     for _ in range(n):
#         p = multiprocessing.Process(target=Chrome1)
#         p.start()
#         processes.append(p)
#     for process in processes:
#         process.join()

def Run(n):
    for i in range(n):
        browserThread = threading.Thread(target=Chrome)
        browserThread.start()