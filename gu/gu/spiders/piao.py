# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from gu.items import GuItem


class PiaoSpider(scrapy.Spider):
    name = 'piao'

    def start_requests(self):
        url = 'http://www.szse.cn/szseWeb/FrontController.szse?'
        for i in range(1, 2+1):
            page = i
            date = {
                'ACTIONID': '7',
                'AJAX': 'AJAX-TRUE',
                'CATALOGID': '1110',
                'TABKEY': 'tab1',
                'tab1PAGENO': str(page),
                'tab1PAGECOUNT': '207',
                'tab1RECORDCOUNT': '2063',
                'REPORT_ACTION': 'navigate'
            }
            header = {'Referer':'http://www.szse.cn/main/marketdata/',
                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
                      }
            yield FormRequest(url=url, formdata=date, headers=header, callback=self.parse)

    def parse(self, response):
        item = GuItem()
        tr = response.xpath('//table[@id="REPORTID_tab1"]//tr')
        for i in tr:
            id = i.xpath('./td[@align="center"][1]//text()').extract_first()
            name_jian = i.xpath('./td[@align="center"][2]//text()').extract_first()
            ip = i.xpath('./td[@align="left"][3]/text()').extract_first()
            if id != None:
                item['id'] = id
            if name_jian != None:
                item['jian'] = name_jian
            if ip != None:
                item['ip'] = ip
                # yield item
