import requests
import threading
import random
from colorama import Fore
import colorama
colorama.init (autoreset = True)

print(f"""
 /\______
 \  ==== --------/|
  | ==== |________|========================================O
 /    ___|-------|      {Fore.WHITE}|{Fore.MAGENTA}     Github Username Checker    {Fore.WHITE}|
 |   /  |               {Fore.WHITE}|{Fore.MAGENTA}                                {Fore.WHITE}|
 |   |_/                {Fore.WHITE}|{Fore.MAGENTA}         Made By:irtco          {Fore.WHITE}|
 |   |                  {Fore.WHITE}|{Fore.MAGENTA}        Discord:irtco#0702      {Fore.WHITE}|
 |   |                  {Fore.WHITE}|{Fore.MAGENTA}        Discord Server:         {Fore.WHITE}|
 |___|                  {Fore.WHITE}|{Fore.MAGENTA}  https://discord.gg/ytrT83ghMp {Fore.WHITE}|
                        {Fore.WHITE}|________________________________|

""")

i=69
number = int(input("How many letters do you want for the usernames to be >> "))
def checker():
    UNIX = 'abcdefghigklmnopqrstuvwxyz123456789-'
    while i<420:
        user = str("".join(random.choice(UNIX)for x in range(int(number))))
        ck = requests.get(f"https://github.com/{user}")
        if ck.status_code == 404:
            print(Fore.GREEN+f"Username Available >> {user}")
            with open("vaild.txt","a+") as file:
                    file.write(user)
                    file.write("\n")
        elif ck.status_code == 200:
            print(Fore.RED+f"Username Unavailable >> {user}")
        else:
            print(Fore.YELLOW+"Something Worng!")
            break


for _ in range(5):
   [].append(threading.Thread(target=checker).start())
for _69_ in []:
   _69_.join()
checker()