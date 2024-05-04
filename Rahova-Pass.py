import os
import sys
import time
from rich.progress import track


def xox(z):
    for a in z + "" :
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.001)

def lod(message):  
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.1)
        
def linex():
     print("\033[1;37m====================================================")  
    
def clear():
    os.system("clear")
    xox(logo)
    
    
logo = ("""
 \033[1;31m ██▀███   ▄▄▄       ██░ ██  ▒█████   ██▒   █▓ ▄▄▄      
 \033[1;31m▓██ ▒ ██▒▒████▄    ▓██░ ██▒▒██▒  ██▒▓██░   █▒▒████▄    
 \033[1;31m▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒ ▓██  █▒░▒██  ▀█▄  
 \033[1;31m▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░  ▒██ █░░░██▄▄▄▄██ 
 \033[1;31m░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓░ ████▓▒░   ▒▀█░   ▓█   ▓██▒
 \033[1;31m░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░    ░ ▐░   ▒▒   ▓▒█░
 \033[1;31m  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░    ░ ░░    ▒   ▒▒ ░
 \033[1;31m  ░░   ░   ░   ▒    ░  ░░ ░░ ░ ░ ▒       ░░    ░   ▒   
 \033[1;31m   ░           ░  ░ ░  ░  ░    ░ ░        ░        ░  ░
\033[1;37m====================================================
 \033[1;32m[•] \033[1;31mAUTHOR    :   \033[1;35mRAHOVA CHARLIN
 \033[1;32m[•] \033[1;32mGITHUB    :   \033[1;34mRahovacharlin
 \033[1;32m[•] \033[1;33mFACEBOOK  :   \033[1;33mRahova charlin
 \033[1;32m[•] \033[1;34mTOOLS     :   \033[1;32mPASSWORD LIST
 \033[1;32m[•] \033[1;35mSTATUS    :   \033[1;31mFREE
\033[1;37m====================================================
\033[1;37m====================================================
        \033[1;37m\033[1;41mTHIS TOOLS CREATED BY RAHOVA CHARLIN\033[0m
\033[1;37m====================================================\n\033[0m""")

             
def main():
    clear()
    linex()
    print("\033[1;32m [1] \033[1;37mAuto password");print("\033[1;32m [2] \033[1;37mManual password ");print("\033[1;32m [0] \033[1;37mExit ")
    linex()
    user1 = input("\n\033[1;31m [?] \033[1;37mChoose : ")
    if user1 in ["1", "01"] :
      Auto()
    if user1 in ["2", "02"] :
      Manual()
    if user1 in ["0", "00"] :
       os.system("clear")
       exit()
    else:
        main()
      
def Auto():
    clear()
    print("\n\033[1;32m [!] \033[1;37mex : \033[1;36m/sdcard/Rahova_Charlin.txt ")
    user3 = input("\n\033[1;32m [+] \033[1;37mFile dump save as : ")
    usera = input ("\n\033[1;32m [?] \033[1;37mVictime first name : ")
    usere = input ("\n\033[1;32m [?] \033[1;37mVictime last name : ")
    list = [usera, usere, usere+usera, usera+usere, usera+"."+usere, usera+"."+usere+"1234", usera+usere+"1234", usera+usere+"@1234", usera+"1234", usere+"1234", usera+"@1234", usere+"@1234",]
    with open(user3, "w+") as f :
         for z in list :
             f.write(z + "\n")
         f.close()
    print("")
    lod("\033[1;32m ➤ Creating file.....")
    print("\n\033[1;32m [√] Your file has been created.")
    input("\n\033[1;36m PRESS ENTER TO MAIN MENU")
    main()
    
    
    
def Manual():
    clear()
    print("\n\033[1;32m [!] \033[1;37mex : \033[1;36m/sdcard/Rahova_Charlin.txt ")
    user3 = input("\n\033[1;32m [+] \033[1;37mFile dump save as : ")
    list = []
    user0 = int(input("\n\033[1;32m [?] \033[1;37mhow many password \033[1;36m(500000000 Max) : "))
    print("")
    for a in range (user0):
        list.append(input(f"\033[1;32m [√] \033[1;37mpassword \033[1;33m{a+1} \033[1;37m: "))
        with open(user3, "w+") as f :
             for z in list :
                 f.write(z + "\n")
             f.close()
    print("")
    lod("\033[1;32m ➤ Creating file.....")
    print("\n\033[1;32m [√] Your file has been created.")
    input("\n\033[1;36m PRESS ENTER TO MAIN MENU")
    main()
         
         
main()