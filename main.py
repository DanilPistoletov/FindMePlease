import webbrowser
print("""
Author site: pistoletoff.ru | FindMePlease ver. 1.5
Github: github.com/DanilPistoletov/FindMePlease/

computerinfo - информация о компьютере
search [запрос] - поиск информации в поисковиках
vk [запрос] - поиск информации по Вконтакте
science [запрос] - поиск по научным базам
social [запрос] - поиск по разным социальным сетям
ok [запрос] - поиск информации по Одноклассникам
domain [домен] - получение информации о домене
ip [IP-адрес] - получение информации об IP-адресе
profile [запрос] - поиск профилей по никам
other [запрос] - поиск информации по прочим источникам
""")

def computerinfo():
    import socket, psutil
    from platform import uname
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Локальный IP-адрес: ", local_ip)
    print("Имя компьютера: ", uname().node)
    print("Операционная система: ", uname().system, uname().release + " | " + uname().version)
    print("Архитектура: ", uname().machine)
    print("Процессор: ", uname().processor)
    print("Количество ядер: ", psutil.cpu_count(logical=False))
    print("Максимальная частота: ", psutil.cpu_freq().max)
    print("Оперативная память: ", psutil.virtual_memory().total / (1024.0 ** 3), "Гб")

def search(request):
    webbrowser.open('https://yandex.ru/search/?text=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://www.google.ru/search?q=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://duckduckgo.com/?t=h_&q=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://www.bing.com/search?q=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://search.yahoo.com/search?p=' + "\"" + request + "\"", new=2)
    webbrowser.open('https://search.brave.com/search?q=' + "\"" + request + "\"", new=2)

def vk(request):
    webbrowser.open('https://vk.com/feed?c%5Bq%5D=' + request + "&c%5Bsort%5D=0&section=search", new=2)
    webbrowser.open('https://vk.com/groups?act=catalog&c%5Bq%5D=' + request, new=2)
    webbrowser.open('https://vk.com/search/people?q=' + request, new=2)
    webbrowser.open('https://vk.com/search/audio?q=' + request, new=2)

def science(request):
    webbrowser.open('https://cyberleninka.ru/search?q=' + request, new=2)
    webbrowser.open('https://scholar.google.com.ru/scholar?q=' + request, new=2)
    webbrowser.open('https://www.researchgate.net/search/publication?q=' + request, new=2)
    webbrowser.open('https://www.isras.ru/search.php?search=' + request, new=2)
    webbrowser.open('https://www.academia.edu/search?q=' + request, new=2)
    webbrowser.open('https://www.refseek.com/search?q=' + request, new=2)
    webbrowser.open('http://www.scholar.ru/search.php?q=' + request, new=2)
    webbrowser.open('https://link.springer.com/search?new-search=true&query=' + request, new=2)

def social(request):
    webbrowser.open('https://www.youtube.com/results?search_query=' + request, new=2)
    webbrowser.open('https://www.tumblr.com/search/' + request, new=2)

def ok(request):
    webbrowser.open('https://ok.ru/dk?st.cmd=searchResult&st.mode=Content&st.query=' + request, new=2)
    webbrowser.open('https://ok.ru/dk?st.cmd=searchResult&st.mode=Users&st.query=' + request, new=2)
    webbrowser.open('https://ok.ru/dk?st.cmd=searchResult&st.mode=Groups&st.query=' + request, new=2)
    webbrowser.open('https://ok.ru/dk?st.cmd=searchResult&st.mode=Music&st.query=' + request, new=2)

def other(request):
    webbrowser.open('https://archive.org/search?query=' + request, new=2)
    webbrowser.open('https://dtf.ru/discovery?q=' + request, new=2)
    webbrowser.open('https://yandex.ru/search/?text=' + "\"" + request + "\"" + " site:doxbin.org", new=2)
    webbrowser.open('https://github.com/search?q=' + request, new=2)

def domain(request):
    import ipwhois, socket
    webbrowser.open('https://web.archive.org/web/20250000000000*/' + request, new=2)
    request = socket.gethostbyname(request)
    whois = str(ipwhois.IPWhois(request).lookup_whois())
    whois = whois.replace(',', ',\n')
    rdap = str(ipwhois.IPWhois(request).lookup_rdap())
    rdap = rdap.replace(',', ',\n')
    print("Whois:\n", whois)
    print("RDAP:\n", rdap)

def ip(request):
    import ipwhois
    whois = str(ipwhois.IPWhois(request).lookup_whois())
    whois = whois.replace(',', ',\n')
    rdap = str(ipwhois.IPWhois(request).lookup_rdap())
    rdap = rdap.replace(',', ',\n')
    print("Whois:\n", whois)
    print("RDAP:\n", rdap)

def profile(request):
    webbrowser.open('https://shikimori.one/' + request, new=2)
    webbrowser.open('https://my.mail.ru/mail/' + request, new=2)

while 1:
    text = input()
    try:
        if text.lower() == "computerinfo":
            computerinfo()
        elif text[:6].lower() == "search":
            search(text[7:])
        elif text[:2].lower() == "vk":
            vk(text[3:])
        elif text[:7].lower() == "science":
            science(text[8:])
        elif text[:6].lower() == "social":
            social(text[7:])
        elif text[:2].lower() == "ok":
            ok(text[3:])
        elif text[:5].lower() == "other":
            other(text[6:])
        elif text[:6].lower() == "domain":
            domain(text[7:])
        elif text[:2].lower() == "ip":
            ip(text[3:])
        elif text[:7].lower() == "profile":
            profile(text[8:])
        else:
            print("Неизвестный запрос")
    except:
        print("Произошла ошибка")