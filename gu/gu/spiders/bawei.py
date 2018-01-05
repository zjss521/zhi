# -*- coding: utf-8 -*-
import requests

data = {'username': 'wg1508B07', 'password': '6666', 'uop':'172.18.5.45'}
url = 'http://172.27.0.200/exam/index.php?m=Index&a=index'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
# header = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"}
r = requests.session()
p = r.post(url=url, headers=header, data=data)
# print(p)
c = r.get('http://172.27.0.200/exam/index.php?m=Index&a=home', headers=header, cookies=p.cookies).text
# print(c)
