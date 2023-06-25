import os,pyperclip,platform
try:
    import pyshorteners
except :
    if platform.system()=="Windows":
        os.system('pip install pyshorteners')
    else:
        os.system('pip3 install pyshorteners')
copied_url=pyperclip.paste()
url=copied_url.strip('https://')
sh=pyshorteners.Shortener()
shorted_url=sh.tinyurl.short(url)
pyperclip.copy(shorted_url)