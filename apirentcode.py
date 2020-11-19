import requests
import time
api = None
def API_get(n):
    global api
    api=n
    print(api)

def So_Du():
    global api
    response = requests.get('https://api.rentcode.net/api/v2/balance?apiKey=' + str(api))
    x = response.json()

    return x['results']['balance']
# lấy id số điện thoại
def Order():
    global api
    a = 'https://api.rentcode.net/api/v2/order/request?apiKey='
    b = '&ServiceProviderId=40&MaximumSms=1&AllowVoiceSms=false'
    c = a + str(api) + b
    print(c)
    response=requests.get(c)
    x = response.json()
    # print(x['id'])
    return x['id']

# Tạo link check SĐT
def TaoLink():
    global api
    a = Order()
    e = str(a)
    b = 'https://api.rentcode.net/api/v2/order/'
    c = '/check?apiKey='
    d = str(b+e+c+str(api))
    print(d)
    return d

# Get SĐT
def GetSDT():
    d = TaoLink()
    SDT = [d]
    # SDT= d
    # print(SDT)
    for i in range(31):
        time.sleep(3)
        response = requests.get(d)
        x = response.json()
        # print(x)
        k = x['phoneNumber']
        print(i)
        if (k != None) and k !='':
            SDT.append(k)
            break
    return SDT


def GetMess(link):

    mess = ''
    for i in range(121):
        time.sleep(3)
        response = requests.get(link)
        x = response.json()
        print(x)
        k = x['message']
        print(i)
        if (k != None) and k != '':
            mess = k
            break
    print(mess)
    s = mess
    x1 = s.find('-')
    print(s[x1 + 1:])
    x2 = s.find(' ')
    ma = s[x1 + 1:x2]
    print(ma)
    return ma


# GetSDT()


# print(GetSDT())

