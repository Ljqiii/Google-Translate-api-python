import execjs
import re
import requests



def getTKK(domainnames=""):
    if (domainnames == ""):
        url = "https://translate.google.com/"
    else:
        url = "https://translate.google." + domainnames + "/"
    #print("url: "+url)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br"}
    googleindexpage = requests.get(url,headers=headers ).text


    pattern=re.compile(r"TKK=(.*?)\(\)\)'\);")
    code=pattern.findall(googleindexpage)

    if(len(code)!=0):
        a=execjs.eval(code[0]+"())')")
        return a
    else:
        return ""

config = {"TKK": ""}

yr = None


def returna(a):
    return

