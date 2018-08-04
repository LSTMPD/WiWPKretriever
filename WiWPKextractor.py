import os
from colorama import init
from colorama import Fore, Style, Back
import time
import subprocess
init()

def screenclean():
    os.system("cls")

print(Fore.CYAN + Style.BRIGHT + """
 ad8888888888ba
dP'         `"8b,
8  -----       "Y888a     ,aaaa,     ,aaa,  ,aa,
8  8   8           "8baaaad    baaaad    baad   8b
8  8   8              """"      """"      ""             8b
8  8   8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  -----       ,d8""
Yb,         ,ad8"
 "Y8888888888P"

""")
time.sleep(1)

print("Vítejte!\n\nZvolte režim:")
print("""
1. WiFi
2. Windows Product Key
""")
mode = input("Režim: ")
if mode == "1":
    screenclean()
    a = 1
    while a == 1:
        os.system("netsh wlan show profile")
        ssid = input("\nZadejte prosím požadované SSID, --exit k ukončení: ")
        if ssid == "--exit":
            break
        else:
            os.system('netsh wlan show profile "' + ssid +  '" key=clear')
            input("\nPro pokračování stiskněte Enter")

if mode == "2":
    screenclean()
    b = 1
    while b == 1:
        WPK = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey"])
        input("\nPro ukončení stiskněte Enter")
        break
