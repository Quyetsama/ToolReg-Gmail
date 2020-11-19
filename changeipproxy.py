import requests

url = "https://proxy-orbit1.p.rapidapi.com/v1/"

headers = {
    'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com",
    'x-rapidapi-key': "7da5185f9amsha01c484dc882bdep1f67fdjsn4e2148eb6d61"
    }

respons = requests.request("GET", url, headers=headers)
x= respons.json()
print(respons.json())
print(x["curl"])

# tách chuỗi ip:port
s = x["curl"]
x1 = s.rfind('/')
ipport = s[x1 + 1:]
print(ipport)


# kết nối ip:port proxy cách 1
# proxies={
#     'https':ipport,
#     'http':ipport
# }
#
# url = 'http://httpbin.org/ip'
#
# resp = requests.get(url,proxies=proxies)
# print(resp.json())


# kết nối ip:port proxy cách 2
from selenium import webdriver
PROXY = ipport # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get("http://whatismyipaddress.com")