import json
import urllib

import requests


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val

def unsigned_right_shitf(n,i):
    n &= 0xffffffff
    return n >> i

def TL(a):
    k = ""
    b = 406644
    b1 = 3293161072

    _b = "+-a^+6"
    Zb = "+-3^+b+-f"

    e = []
    for g in range(len(a)):
        m = ord(a[g])
        if 128 > m :
            e.append(m)
        else:
            if 2048 > m:
                e.append(m >> 6 | 192)
            else:
                if (55296 == (m & 64512)) and (g + 1) < len(a) and (56320 == ord(a[g + 1]) & 64512):
                    m = 65536 + ((m & 1023) << 10) + ord(a[g]) & 1023
                    e.append(m >> 18 | 240)
                    e.append(m >> 12 & 63 | 128)                    
                else:
                    e.append(m >> 12 | 224)
                    e.append(m >> 6 & 63 | 128)
                    e.append(m & 63 | 128)
    
    a = b
    for f in range(len(e)):
        a += e[f]
        a = RL(a, _b)
    a = RL(a, Zb)
    a = a & 0xffffffff if 0 > a else a
    a = a ^ b1
    if 0 > a:
        a = (a & 2147483647) + 2147483648
    a %= 1E6
    float_part = str(int((int(a) ^ int(b))))
    return f"{int(a)}.{float_part}"

def RL(a, b):
    t = "a"; 
    Yb = "+"; 
    c = 0
    while c < len(b) - 2:
        d = b[c+2]
        d = ord(d[0])-87 if d >= t else int(d)
        d = unsigned_right_shitf(a, d) if b[c+1] == Yb else int_overflow(a<<d)
        a = a + int_overflow(d&0xffffffff) if b[c] == Yb else int_overflow(a^d)
        c += 3

    return a

def buildUrl(content, tk, tl):  
        baseUrl = 'http://translate.google.cn/translate_a/single'
        baseUrl += '?client=webapp&'
        baseUrl += 'sl=auto&'
        baseUrl += 'tl=' + str(tl) + '&'
        baseUrl += 'hl=zh-CN&'
        baseUrl += 'dt=at&'
        baseUrl += 'dt=bd&'
        baseUrl += 'dt=ex&'
        baseUrl += 'dt=ld&'
        baseUrl += 'dt=md&'
        baseUrl += 'dt=qca&'
        baseUrl += 'dt=rw&'
        baseUrl += 'dt=rm&'
        baseUrl += 'dt=ss&'
        baseUrl += 'dt=t&'
        baseUrl += 'ie=UTF-8&'
        baseUrl += 'oe=UTF-8&'
        baseUrl += 'clearbtn=1&'
        baseUrl += 'otf=1&'
        baseUrl += 'pc=1&'
        baseUrl += 'srcrom=0&'
        baseUrl += 'ssel=0&'
        baseUrl += 'tsel=0&'
        baseUrl += 'kc=2&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + content
        return baseUrl

def en_to_cn(txt):
    tl = "zh-CN"  # tl is the target language 
    tk = TL(txt)

    content = urllib.parse.quote(txt)
    url = buildUrl(content, tk, tl)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    r = requests.get(url,headers=headers,timeout=3)
    r_json = json.loads(r.text)
    return r_json

def cn_to_en(txt):
        tl = "en" # tl is the target language 
        tk = TL(txt)

        content = urllib.parse.quote(txt)
        url = buildUrl(content, tk,tl) 
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        r = requests.get(url,headers=headers,timeout=3)
        r_json = json.loads(r.text)
        return r_json



print(cn_to_en("COVID-19 终将被战胜"))
print(en_to_cn("COVID-19 will eventually be defeated"))
