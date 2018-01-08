import requests
import json
import pymongo
# http://tomcat.shenhuangtech.cn:8099/Markup350/services/element/value.json?_dc=1515323984276&ref=true&timestamp=1515324481118&id=19683850
# http://tomcat.shenhuangtech.cn:8099/Markup350/services/element/value.json?_dc=1515325389034&ref=true&timestamp=1515325015921&id=19683851
import time


class Huang:
    def __init__(self):
        self.url = 'http://tomcat.shenhuangtech.cn:8099/Markup350/services/task/listprogress.json?_dc=1515325553504&categoryId=343&keyword=&page=1&start=0&limit=25'
        self.header = {'Cookie':'JSESSIONID=B2D15D7CB2E0D85C9E60803C76F293F8; username=%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%91%98; password=shenhuangbiaoyin; remember=true',
                       "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"}
        self.db = pymongo.MongoClient()
        self.db_name = self.db['神皇标引']
        self.table = self.db_name['shen']

    def get_html(self):
        response = requests.get(self.url, headers=self.header).text
        # print(response)
        self.get_json(response)

    def get_json(self, html):
        json_url = json.loads(html)
        id = json_url["progresses"]

        for i in id:
            name = i["bookName"]
            jie = i['id']+1
            url = 'http://tomcat.shenhuangtech.cn:8099/Markup350/services/element/value.json?_dc=1515325389034&ref=true&timestamp=1515325015921&id='+str(jie)
            print(url)
            time.sleep(3)
            self.get_url(url, name)

    def get_url(self, url, name):
        data = {}
        response = requests.get(url, headers=self.header).text
        json_value = json.loads(response)
        value = json_value["element"]["value"]
        data['name'] = name
        data['value'] = value
        self.table.insert_one(data)
        print('loading...')

if __name__ == '__main__':
    q = Huang()
    q.get_html()