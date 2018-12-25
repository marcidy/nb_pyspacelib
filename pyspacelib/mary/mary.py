import requests
from httpish import GET200, POST200, GET
import re

BASE = "http://pegasus.noise"


def mute():
    return request.get(BASE+"/mute/")


def unmute():
    return request.get(BASE+"/unmute/")


def say(text):
    return requests.post(BASE+"/say/", data={'txt': text})


def setLanguage(code):
    return requests.post(BASE+"/lang/", data={'lang': code})


def getLanguage():
    c = request.get(BASE+"/lang/")
    c.expect200()
    c.recvuntil("selected>")
    lang = c.recvuntil("<")[0:-1].strip()
    c.recvuntil("</html>")
    c.close()
    return lang


def getLanguages():
    c = requests.get(BASE+"/lang/")
    c.expect200()
    c.recvuntil('<select name="lang">')
    options = c.recvuntil("</select>").strip()
    c.recvuntil("</html>")
    c.close()
    return re.split(r"\s+", re.sub(r'<[^>]+>', " ", options))[1:-1]
