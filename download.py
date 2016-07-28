import urllib
import sys
import os

def make_dir():
    os.mkdir('./nhk_kifu')
def download():
    count = 0
    for i in range(1000000):
        url = "http://www.kihuu.net/sgf/k" + ("00000000000" + str(i))[-11:] + ".sgf"
        ftitle = str(i-count+1) + ".sgf"
        urllib.urlretrieve(url, './nhk_kifu/{0}'.format(ftitle))
        fsize = os.path.getsize('./nhk_kifu/{0}'.format(ftitle))
        if fsize == 0:
            os.remove('./nhk_kifu/{0}'.format(ftitle))
            count += 1
if __name__ == "__main__":
    make_dir()
    download()

