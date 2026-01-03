import os
import sys
import httpx
from colorama import Fore, init
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fw = Fore.WHITE
fre = Fore.RESET

list = [ 
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt',
'https://proxyspace.pro/',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt',
'https://spys.one/free-proxy-list/',
'https://www.proxy-list.download/api/v1/get?type=http&anon=elite&country=US',
'https://www.proxy-list.download/api/v1/get?type=http&anon=transparent&country=US',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'http://worm.rip/http.txt',
'http://alexa.lr2b.com/proxylist.txt',
'https://api.openproxylist.xyz/http.txt',
'http://rootjazz.com/proxies/proxies.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/Firdoxx/proxy-list/main/https',
'https://raw.githubusercontent.com/Firdoxx/proxy-list/main/http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
'https://raw.githubusercontent.com/Jakee8718/Free-Proxies/main/proxy/-http%20and%20https.txt',
'https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt',
'https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/https.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all',
'https://www.proxy-list.download/api/v1/get?type=socks5',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt',
'https://github.com/hookzof/socks5_list/blob/master/proxy.txt',
'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-http.txt',
'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-https.txt',
'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-socks4.txt',
'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies-socks5.txt',
'https://github.com/jetkai/proxy-list/blob/main/online-proxies/txt/proxies.txt',
'https://raw.githubusercontent.com/a2u/free-proxy-list/master/free-proxy-list.txt',
'https://raw.githubusercontent.com/mishakorzik/Free-Proxy/main/proxy.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
'https://slims-sf.com/Htewarukofdcn/proxy.txt',
'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt',
'https://api.proxyscrape.com/v2/?request=displayproxies',
'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://slims-sf.com/Htewarukofdcn/https.txt',
'https://slims-sf.com/Htewarukofdcn/http.txt',
]  
         

if __name__ == "__main__":
    file = "proxy.txt"
    
    try:
        if os.path.isfile(file):
            os.system('cls' if os.name == 'nt' else 'clear')
            os.remove(file)
            print("{}File {} \n{}Wait {} file is still creating\n".format(fr, file, fy, file))
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| installing proxy {}{}".format(fg, proxy))
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            with open(file, 'a') as data:
                for proxy in list:
                    data.write(httpx.get(proxy).text)
                    print(" -| mengambil {}{}".format(fg, proxy))
    
        with open(file, 'r') as count:
            total = sum(1 for line in count)
        print("\n{}( {}{} {}) {}Proxy successfully created.". format(fw, fy, total, fw, fg))
    
    except IndexError:
        sys.exit(1)
        
