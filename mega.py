import time
import urllib
import sys
import os

os.system('clear')

bar = "\033[1;33;40m\n_________________________________________________\n"

name = """\033[1;32;40m
___________________________________________________________
\033[1;36;40m      __  __               _      ____        _   _
\033[1;34;40m     |  \/  | ___  __ _   / \    |  _ \ _   _| \ | |
\033[1;36;40m     | |\/| |/ _ \/ _` | / O \   | |_) | | | |  \| |
\033[1;34;40m     | |  | |  __/ (_| |/ ___ \  |  _ <| |_| | |\  |
\033[1;36;40m     |_|  |_|\___|\__, /_/   \_\ |_| \_\\____/|_| \_|
\033[1;34;40m                  |___/

\033[1;35;40m              [+] Tool By ERROR KILLER
\033[1;32;40m___________________________________________________________
"""
print(name, "")


try:
    f = open("auth.txt", "r")
    auth = f.read()
    f.close 
except:
    wr = str(input("\033[1;0;40mPaste Your Auth here :- "))
    f = open("auth.txt", "w")
    f.write(wr)
    f.close
    f = open("auth.txt", "r")
    auth = f.read()
    f.close

try:
    f = open("url.txt", "r")
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = str(input("Paste Your URL here :- "))
    f = open("url.txt", "w")
    f.write(wr)
    f.close
    f = open("url.txt", "r")
    url1 = f.read()
    f.close

try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name,"\n")
    s = int(input("\033[1;0;40mEnter Amount - "))
    header = {"Host": "megarun.dialog.lk",
              "Authorization": auth, "X-Unity-Version": "2018.3.0f2"}
    url = url1
    
    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers=header)
        resp = str(res)
        if resp == '<Response [204]>':
            print(bar)
            print("\n\033[1;32;40m [+] No Data ... [+]")
            print(bar)  
        elif resp == '<Response [200]>':
            print(bar)
            print("\n\033[1;32;40m [+] You Won Check Balance ... [+]")
            print(bar)
        else:
            print(bar)
            print("\n\033[1;31;40m [+] Check Again, I think You are Blocked User... [+]")
            print(bar)
        

        ss+=1
        print("\033[1;0;40m\n",str(ss), "Please Wait For Next request",end="")
        for i in range(180):
            
            pr = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
