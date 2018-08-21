from abc import abstractclassmethod
from getTKK import getTKK
import time
import ctypes
import requests





class GoogleTranslate():


    def __init__(self, sl='', tl='', domainnames=""):
        """
        A python wrapped free and unlimited API for Google Translate.

        :param sl:from Language
        :param tl:to Language
        :param domainnames: google domainnames, for example if domainnames="com" ,the url is "translate.google.com". In China the com domainnames is blocked by GFW,you can use "cn".
        """
        self.sl = sl
        self.tl = tl
        self.hl = tl



        if(domainnames==""):
            self.domainnames ="com"
        else:
            self.domainnames = domainnames

        self.TKK = getTKK(domainnames=self.domainnames)

    def _returnintorzero(self,d):
        try:
            temp = int(d)
        except:
            temp = 0
        return temp

    def _xr(self, a, b):
        size_b = len(b)
        c = 0
        while c < size_b - 2:
            d = b[c + 2]
            d = ord(d[0]) - 87 if 'a' <= d else int(d)
            d = (a % 0x100000000) >> d if '+' == b[c + 1] else a << d
            a = a + d & 4294967295 if '+' == b[c] else a ^ d
            c += 3
        return a

    def trans(self,text):
        """
        translate text

        :param text: The text to be translate

        :return:
        """
        tk=self._gettk(text)

        timeh = int(time.time() / 3600)
        if (self.TKK.split(".")[0]!=timeh):
            self.TKK = getTKK(domainnames=self.domainnames)

        data = {
            "client": 't',
            "sl": self.sl,
            "tl": self.tl,
            "hl": self.hl,
            "dt": ['at', 'bd', 'ex', 'ld', 'md', 'qca', 'rw', 'rm', 'ss', 't'],
            "ie": 'UTF-8',
            "oe": 'UTF-8',
            "otf": 1,
            "ssel": 0,
            "tsel": 0,
            "kc": 7,
            "q": text,
            "tk": tk
        };

        url='https://translate.google.'+self.domainnames+'/translate_a/single';

        jsonres=requests.get(url=url,params=data)
        return jsonres.json()[0][0][0]



    def _gettk(self,a):

        # print(self.TKK)
        d = self.TKK.split(".")
        b = int(d[0])
        e = []
        for g in range(len(a)):
            l = ord(a[g])
            if (128 > l):
                e.append(l)
            else:
                if (2048 > l):
                    e.append(l >> 6 | 192)
                else:
                    if (55296 == (l & 64512) and g + 1 < len(a) and 56320 == (ord(a[g + 1]) & 64512)):
                        l = 65536 + ((l & 1023) << 10) + (a.charCodeAt(++g) & 1023)
                        e.append(l >> 18 | 240)
                        e.append(l >> 12 & 63 | 128)
                    else:
                        e.append(l >> 12 | 224)
                        e.append(l >> 6 & 63 | 128)
                    e.append(l & 63 | 128)

        a = b
        for f in range(len(e)):
            a = a + int(e[f])
            a = self._xr(a, "+-a^+6")
        a = self._xr(a, "+-3^+b+-f");
        a ^=self._returnintorzero(d[1])
        if(0>a):
            a = (a & 2147483647) + 2147483648
        a %= 1E6;
        return str(int(a))+ "." + str(int(a) ^ b)






a = GoogleTranslate(domainnames="cn",sl="en",tl="zh-CN")


print(a.trans("I am a boy and she is a girl."))
print(a.trans("She is a girl."))
