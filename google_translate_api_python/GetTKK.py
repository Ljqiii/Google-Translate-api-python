
import re
import requests



def getTKK(domainnames=""):
    if (domainnames == ""):
        url = "https://translate.google.com/"
    else:
        url = "https://translate.google." + domainnames + "/"

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br"}
    googleindexpage = requests.get(url,headers=headers ).text


    tkk=re.findall("tkk:'(\d*\.\d*)'",googleindexpage)


    if(len(tkk)!=0):
        return tkk[0]
    else:
        return None

config = {"TKK": ""}

yr = None


def returna(a):
    return

getTKK('cn')

