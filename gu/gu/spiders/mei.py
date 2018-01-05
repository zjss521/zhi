# -*- coding: utf-8 -*-
import scrapy
from flask import json
from scrapy.http import Request
from gu.items import GuItem


class MeiSpider(scrapy.Spider):
    name = 'mei'
    # allowed_domains = ['www.meishichina.com']

    def start_requests(self):
        for i in range(1, 2+1):
            urls = 'http://home.meishichina.com/ajax/ajax.php?ac=recipe&op=getMoreDiffStateRecipeList&classid=0&orderby=hot&page={}'.format(i)
            yield Request(url=urls, callback=self.parse)

    def parse(self, response):
        jie_xi = response.text
        get_json = json.loads(jie_xi)["data"]
        for i in get_json:
            c = i["id"]
            url = 'http://home.meishichina.com/recipe-'+str(c)+'.html'
            yield Request(url, callback=self.get_html)

    def get_html(self, response):
        item = GuItem()
        name = response.css('.recipe_De_title a::attr(title)').extract_first()
        print(name)
        cai = response.xpath('//div[@class="recipeCategory_sub_R clear"]/ul')
        for i in cai:
            pu = i.xpath('//div[@class="recipeCategory_sub_R clear"]//span//b/text()').extract()
            liang = i.xpath('//div[@class="recipeCategory_sub_R clear"]//span[2]/text()').extract()
            list = []
            for p, l in zip(pu, liang):
                c = (p+':'+l)
                list.append(c)
            item['id'] = list
                # item['jian'] = l
            print(item)