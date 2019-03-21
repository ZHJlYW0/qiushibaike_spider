# coding=utf-8
import json

import requests
from lxml import etree


class QiushibaikeSpider(object):
    def __init__(self):
        self.Request_URL_temp = 'https://www.qiushibaike.com/hot/page/{}/'
        self.Request_Headers = {'Referer': 'https://www.qiushibaike.com/',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}

    def get_url_list(self):
        """1.根据url地址的规律url_list"""
        url_list = [self.Request_URL_temp.format(i) for i in range(1, 14)]
        return url_list

    def parse_url(self, url):
        """2.发送请求，获取响应"""
        print('正在解析：', url)
        response = requests.get(url, headers=self.Request_Headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        """3.提取数据"""
        html_object = etree.HTML(html_str)
        print('---html_object---\n', html_object)
        # 分组
        # col1 = html_object.xpath('//div[@class="col1"]/div')
        # print('---col1---\n', col1)
        object_list = html_object.xpath('//div[@id="content-left"]/div')
        print('---object_list---\n', object_list)
        content_list = list()
        for object in object_list:
            content = dict()
            try:
                content['作者'] = object.xpath('.//div[@class="author clearfix"]/a/h2/text()')
                content['作者'] = [i.strip() for i in content['作者']]
            except:
                content['作者'] = None
            try:
                content['内容'] = object.xpath('.//div[@class="content"]/span/text()')
                content['内容'] = [i.strip() for i in content['内容']]
            except:
                content['内容'] = None
            try:
                content['好笑数'] = object.xpath('.//span[@class="stats-vote"]/i[@class="number"]/text()')
            except:
                content['好笑数'] = None
            try:
                content['评论数'] = object.xpath('.//span[@class="stats-comments"]/a/i[@class="number"]/text()')
            except:
                content['评论数'] = None
            try:
                content['图片'] = object.xpath('.//div[@class="thumb"]/a/img/@src')
            except:
                content['图片'] = None
            content_list.append(content)
        return content_list

    def save_content_list(self, content_list):
        """4.保存"""
        with open('糗事百科24小时爆笑笑话大全.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                # print(content)
                # f.write(str(content))  # 有些字符会无法识别
                f.write(json.dumps(content, ensure_ascii=False))  # 使用utf-8
                f.write('\n')
        print('保存成功')

    def run(self):
        # 1.根据url地址的规律url_list
        url_list = self.get_url_list()
        # 2.发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiushibaike = QiushibaikeSpider()
    qiushibaike.run()
"""
/home/python/.virtualenvs/spider_py3/bin/python /home/python/6节课掌握Python爬虫_代码/09_糗事百科爬虫.py
正在解析： https://www.qiushibaike.com/hot/page/1/
---html_object---
 <Element html at 0x7f70071a39c8>
---object_list---
 [<Element div at 0x7f7003a30808>, <Element div at 0x7f7003a30c08>, <Element div at 0x7f7003a30bc8>, <Element div at 0x7f7003a30c48>, <Element div at 0x7f7003a30b88>, <Element div at 0x7f7003a30dc8>, <Element div at 0x7f7003a30cc8>, <Element div at 0x7f7003a30248>, <Element div at 0x7f7003a30e88>, <Element div at 0x7f7003190bc8>, <Element div at 0x7f7003190a08>, <Element div at 0x7f7003190b08>, <Element div at 0x7f7003190c48>, <Element div at 0x7f7003190c88>, <Element div at 0x7f7003190cc8>, <Element div at 0x7f7003190b48>, <Element div at 0x7f7003a3cb48>, <Element div at 0x7f7003a3ca08>, <Element div at 0x7f7003a3ca48>, <Element div at 0x7f7003a3c9c8>, <Element div at 0x7f7003a3cb08>, <Element div at 0x7f7003a3cbc8>, <Element div at 0x7f7003a3cc88>, <Element div at 0x7f7003a3c648>, <Element div at 0x7f7003a3c448>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/2/
---html_object---
 <Element html at 0x7f700461a708>
---object_list---
 [<Element div at 0x7f7008b7b048>, <Element div at 0x7f7003a29648>, <Element div at 0x7f7003a29508>, <Element div at 0x7f7003a29608>, <Element div at 0x7f7003a29348>, <Element div at 0x7f7003a29b48>, <Element div at 0x7f7003a295c8>, <Element div at 0x7f7003190188>, <Element div at 0x7f7003190cc8>, <Element div at 0x7f7003190c88>, <Element div at 0x7f7003190b48>, <Element div at 0x7f7003190888>, <Element div at 0x7f7003190088>, <Element div at 0x7f7003190b88>, <Element div at 0x7f70071a39c8>, <Element div at 0x7f70031af788>, <Element div at 0x7f70031af808>, <Element div at 0x7f70031afc88>, <Element div at 0x7f7003a3c648>, <Element div at 0x7f7003a3cc88>, <Element div at 0x7f7003a3c348>, <Element div at 0x7f7003a3c108>, <Element div at 0x7f7003a3c4c8>, <Element div at 0x7f7003a3c388>, <Element div at 0x7f7003a3cb08>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/3/
---html_object---
 <Element html at 0x7f7008b7b588>
---object_list---
 [<Element div at 0x7f7008b7bf88>, <Element div at 0x7f700319ad08>, <Element div at 0x7f70046c9fc8>, <Element div at 0x7f7003a30ec8>, <Element div at 0x7f7003a30fc8>, <Element div at 0x7f7003a30a48>, <Element div at 0x7f7003a30f08>, <Element div at 0x7f7008b72e88>, <Element div at 0x7f7004644688>, <Element div at 0x7f7004644308>, <Element div at 0x7f7004644248>, <Element div at 0x7f7004644908>, <Element div at 0x7f7004644748>, <Element div at 0x7f7004644888>, <Element div at 0x7f7004646148>, <Element div at 0x7f70031b32c8>, <Element div at 0x7f70031b3588>, <Element div at 0x7f70031ab608>, <Element div at 0x7f70031abc08>, <Element div at 0x7f70031aba88>, <Element div at 0x7f70031ab688>, <Element div at 0x7f70031ab508>, <Element div at 0x7f70031ab808>, <Element div at 0x7f70031ab408>, <Element div at 0x7f70031abb08>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/4/
---html_object---
 <Element html at 0x7f7005480bc8>
---object_list---
 [<Element div at 0x7f70031af908>, <Element div at 0x7f70031afd48>, <Element div at 0x7f70031afc48>, <Element div at 0x7f70031af5c8>, <Element div at 0x7f70031b7c88>, <Element div at 0x7f70031901c8>, <Element div at 0x7f7003190048>, <Element div at 0x7f7003190148>, <Element div at 0x7f7003190288>, <Element div at 0x7f7003190208>, <Element div at 0x7f7003190588>, <Element div at 0x7f7003190a08>, <Element div at 0x7f70031b6748>, <Element div at 0x7f70031b6048>, <Element div at 0x7f70031b6108>, <Element div at 0x7f7003a30808>, <Element div at 0x7f7003a30c48>, <Element div at 0x7f7003a30f48>, <Element div at 0x7f7003a30bc8>, <Element div at 0x7f7003a30ec8>, <Element div at 0x7f7003a30d48>, <Element div at 0x7f7003a30cc8>, <Element div at 0x7f7003a30e08>, <Element div at 0x7f7003a30d88>, <Element div at 0x7f700319a308>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/5/
---html_object---
 <Element html at 0x7f7004646308>
---object_list---
 [<Element div at 0x7f700461a388>, <Element div at 0x7f70071a3908>, <Element div at 0x7f7003a3ca08>, <Element div at 0x7f7003a3cbc8>, <Element div at 0x7f7003a3c208>, <Element div at 0x7f7003a3c3c8>, <Element div at 0x7f7003a3c4c8>, <Element div at 0x7f7003a3c688>, <Element div at 0x7f7003a3c048>, <Element div at 0x7f7003a309c8>, <Element div at 0x7f7003a30c48>, <Element div at 0x7f70031b9288>, <Element div at 0x7f70031b9488>, <Element div at 0x7f70031b9388>, <Element div at 0x7f70031b9588>, <Element div at 0x7f70031b9708>, <Element div at 0x7f70031b9a88>, <Element div at 0x7f7003a29588>, <Element div at 0x7f7003a29548>, <Element div at 0x7f7003a29488>, <Element div at 0x7f7003a29148>, <Element div at 0x7f7003a29048>, <Element div at 0x7f7003a29748>, <Element div at 0x7f7003a291c8>, <Element div at 0x7f7003a29708>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/6/
---html_object---
 <Element html at 0x7f70031b7c48>
---object_list---
 [<Element div at 0x7f70046c9fc8>, <Element div at 0x7f7003a1cf08>, <Element div at 0x7f7003a1ce48>, <Element div at 0x7f7004644748>, <Element div at 0x7f7004644308>, <Element div at 0x7f7004644808>, <Element div at 0x7f7004644508>, <Element div at 0x7f7004644248>, <Element div at 0x7f7004644688>, <Element div at 0x7f70031b66c8>, <Element div at 0x7f70031b6248>, <Element div at 0x7f70031b6188>, <Element div at 0x7f70031b6548>, <Element div at 0x7f70031b6148>, <Element div at 0x7f70031b6788>, <Element div at 0x7f70031b68c8>, <Element div at 0x7f70031b6988>, <Element div at 0x7f7008b72e88>, <Element div at 0x7f700319a588>, <Element div at 0x7f700319a708>, <Element div at 0x7f700319a788>, <Element div at 0x7f700319a448>, <Element div at 0x7f700319a648>, <Element div at 0x7f700319aa08>, <Element div at 0x7f700319a888>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/7/
---html_object---
 <Element html at 0x7f7004646288>
---object_list---
 [<Element div at 0x7f700461a4c8>, <Element div at 0x7f70031ab148>, <Element div at 0x7f70031ab1c8>, <Element div at 0x7f70031abb88>, <Element div at 0x7f70031abf48>, <Element div at 0x7f70031ab108>, <Element div at 0x7f7003a3cb08>, <Element div at 0x7f7003a3cdc8>, <Element div at 0x7f7003a3c348>, <Element div at 0x7f7003a3c388>, <Element div at 0x7f7003a3cec8>, <Element div at 0x7f7003a3cd88>, <Element div at 0x7f7003a3cb88>, <Element div at 0x7f7003a3c9c8>, <Element div at 0x7f70031b9348>, <Element div at 0x7f70031b9408>, <Element div at 0x7f70031b9988>, <Element div at 0x7f70031b9208>, <Element div at 0x7f70031b9548>, <Element div at 0x7f70031b9648>, <Element div at 0x7f70031b9748>, <Element div at 0x7f70031b9948>, <Element div at 0x7f70071a39c8>, <Element div at 0x7f7003a30fc8>, <Element div at 0x7f7003a30a08>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/8/
---html_object---
 <Element html at 0x7f7004644548>
---object_list---
 [<Element div at 0x7f7003a29888>, <Element div at 0x7f7003a29948>, <Element div at 0x7f7003a29808>, <Element div at 0x7f7003a29388>, <Element div at 0x7f70031b33c8>, <Element div at 0x7f700319acc8>, <Element div at 0x7f700319ac48>, <Element div at 0x7f700319a7c8>, <Element div at 0x7f700319a048>, <Element div at 0x7f700319a748>, <Element div at 0x7f700319a908>, <Element div at 0x7f700461a4c8>, <Element div at 0x7f7003190a88>, <Element div at 0x7f70031900c8>, <Element div at 0x7f70031ab448>, <Element div at 0x7f70031ab108>, <Element div at 0x7f70031abf48>, <Element div at 0x7f70031abdc8>, <Element div at 0x7f70031ab048>, <Element div at 0x7f70031ab148>, <Element div at 0x7f70031ab408>, <Element div at 0x7f70031ab1c8>, <Element div at 0x7f70031abb88>, <Element div at 0x7f70031abc88>, <Element div at 0x7f70031afb48>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/9/
---html_object---
 <Element html at 0x7f7003a30e88>
---object_list---
 [<Element div at 0x7f7008b7b048>, <Element div at 0x7f7008b7bf88>, <Element div at 0x7f70031b7088>, <Element div at 0x7f70031b7188>, <Element div at 0x7f70031b7308>, <Element div at 0x7f70031b7208>, <Element div at 0x7f70031b7608>, <Element div at 0x7f70031b7348>, <Element div at 0x7f7003a1ce88>, <Element div at 0x7f7003a1cfc8>, <Element div at 0x7f7003a1ce48>, <Element div at 0x7f70031b6448>, <Element div at 0x7f70031b6ac8>, <Element div at 0x7f70031b64c8>, <Element div at 0x7f70031b6fc8>, <Element div at 0x7f70031b6848>, <Element div at 0x7f70031b6908>, <Element div at 0x7f70031b6f08>, <Element div at 0x7f7003a292c8>, <Element div at 0x7f7003a296c8>, <Element div at 0x7f7003a29688>, <Element div at 0x7f7003a29308>, <Element div at 0x7f7003a29708>, <Element div at 0x7f7003a29148>, <Element div at 0x7f70031b3b48>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/10/
---html_object---
 <Element html at 0x7f70031b96c8>
---object_list---
 [<Element div at 0x7f70031b9a88>, <Element div at 0x7f70031af188>, <Element div at 0x7f70031af948>, <Element div at 0x7f70031af848>, <Element div at 0x7f70031af308>, <Element div at 0x7f70031afac8>, <Element div at 0x7f70031c1bc8>, <Element div at 0x7f70031c1cc8>, <Element div at 0x7f70031c1c48>, <Element div at 0x7f70031c1dc8>, <Element div at 0x7f70031c1fc8>, <Element div at 0x7f70031c1208>, <Element div at 0x7f70031c10c8>, <Element div at 0x7f70031c19c8>, <Element div at 0x7f70031c18c8>, <Element div at 0x7f70031c1a48>, <Element div at 0x7f70031c1ac8>, <Element div at 0x7f70031c1188>, <Element div at 0x7f70031ab2c8>, <Element div at 0x7f70031ab0c8>, <Element div at 0x7f70031ab5c8>, <Element div at 0x7f70031ab648>, <Element div at 0x7f70031abc08>, <Element div at 0x7f70031ab3c8>, <Element div at 0x7f70031ab588>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/11/
---html_object---
 <Element html at 0x7f7005480c48>
---object_list---
 [<Element div at 0x7f7003a3cac8>, <Element div at 0x7f7003a3ce08>, <Element div at 0x7f70031b73c8>, <Element div at 0x7f70031b6a08>, <Element div at 0x7f70031b6bc8>, <Element div at 0x7f70031b6a48>, <Element div at 0x7f70031b6688>, <Element div at 0x7f70031b6388>, <Element div at 0x7f70031b6648>, <Element div at 0x7f70031b6188>, <Element div at 0x7f700319a5c8>, <Element div at 0x7f700319acc8>, <Element div at 0x7f700319a888>, <Element div at 0x7f70031c2548>, <Element div at 0x7f70031c26c8>, <Element div at 0x7f70031c25c8>, <Element div at 0x7f70031c2748>, <Element div at 0x7f70031c2908>, <Element div at 0x7f70031c2348>, <Element div at 0x7f70031c23c8>, <Element div at 0x7f70031c24c8>, <Element div at 0x7f7003190bc8>, <Element div at 0x7f7003190808>, <Element div at 0x7f70031907c8>, <Element div at 0x7f70031903c8>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/12/
---html_object---
 <Element html at 0x7f7003a1cb08>
---object_list---
 [<Element div at 0x7f70031c1248>, <Element div at 0x7f70031ab808>, <Element div at 0x7f70031ab6c8>, <Element div at 0x7f7003a30bc8>, <Element div at 0x7f7008b7b048>, <Element div at 0x7f7003a3c188>, <Element div at 0x7f7003a3c308>, <Element div at 0x7f7003a3c688>, <Element div at 0x7f7003a3cb88>, <Element div at 0x7f7003a3ce48>, <Element div at 0x7f7003a3ce08>, <Element div at 0x7f7003a3cb08>, <Element div at 0x7f70031af688>, <Element div at 0x7f70031af288>, <Element div at 0x7f70031b3788>, <Element div at 0x7f70031b3a48>, <Element div at 0x7f70031b3608>, <Element div at 0x7f70031b3d08>, <Element div at 0x7f70031b3248>, <Element div at 0x7f70031b3108>, <Element div at 0x7f70031b39c8>, <Element div at 0x7f70031b3208>, <Element div at 0x7f70031b31c8>, <Element div at 0x7f70031b3488>, <Element div at 0x7f70031b35c8>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/13/
---html_object---
 <Element html at 0x7f70031c21c8>
---object_list---
 [<Element div at 0x7f70031c2ac8>, <Element div at 0x7f70031b7b08>, <Element div at 0x7f70031c1408>, <Element div at 0x7f70031c1588>, <Element div at 0x7f70031c14c8>, <Element div at 0x7f70031c1ac8>, <Element div at 0x7f70031900c8>, <Element div at 0x7f7003190288>, <Element div at 0x7f7003190088>, <Element div at 0x7f7003190b88>, <Element div at 0x7f7003190a08>, <Element div at 0x7f7003190188>, <Element div at 0x7f7003190148>, <Element div at 0x7f7004644908>, <Element div at 0x7f70031abb48>, <Element div at 0x7f70031ab048>, <Element div at 0x7f70031ab0c8>, <Element div at 0x7f70031ab588>, <Element div at 0x7f70031ab6c8>, <Element div at 0x7f70031abc88>, <Element div at 0x7f70031abcc8>, <Element div at 0x7f70031ab948>, <Element div at 0x7f70031abf88>, <Element div at 0x7f70031ab208>, <Element div at 0x7f70031abf08>]
保存成功

Process finished with exit code 0
"""
