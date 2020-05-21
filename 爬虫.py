from urllib.request import *

url = 'http://www.baidu.com'
with urlopen(url) as response:
    print(response.getheader('server'))
    print(response.geturl())
    print(response.version)
    print(response.getcode)