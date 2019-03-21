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

    def open_document(self):
        self.f = open('糗事百科24小时爆笑笑话大全2.txt', 'a', encoding='utf-8')
        print('打开文件')

    def save_content_list(self, content_list):
        """4.保存"""
        for content in content_list:
            # print(content)
            # self.f.write(str(content))  # 有些字符会无法识别
            self.f.write(json.dumps(content, ensure_ascii=False))  # 使用utf-8
            self.f.write('\n')
        print('保存成功')

    def close_document(self):
        self.f.close()
        print('关闭文件')

    def run(self):
        # 1.根据url地址的规律url_list
        url_list = self.get_url_list()
        # 打开文件
        self.open_document()
        # 2.发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存
            self.save_content_list(content_list)
        # 关闭文件
        self.close_document()


if __name__ == '__main__':
    qiushibaike = QiushibaikeSpider()
    qiushibaike.run()
"""
/home/python/.virtualenvs/spider_py3/bin/python /home/python/6节课掌握Python爬虫_代码/09_糗事百科爬虫_02.py
打开文件
正在解析： https://www.qiushibaike.com/hot/page/1/
---html_object---
 <Element html at 0x7f7e59e30ac8>
---object_list---
 [<Element div at 0x7f7e55e1ed88>, <Element div at 0x7f7e55e1ebc8>, <Element div at 0x7f7e55e1ecc8>, <Element div at 0x7f7e55e1ee88>, <Element div at 0x7f7e55e1ee48>, <Element div at 0x7f7e55e1ee08>, <Element div at 0x7f7e55e1ed08>, <Element div at 0x7f7e566c90c8>, <Element div at 0x7f7e566c9c08>, <Element div at 0x7f7e566c9b88>, <Element div at 0x7f7e566c9848>, <Element div at 0x7f7e566c9e48>, <Element div at 0x7f7e566c9d08>, <Element div at 0x7f7e566c9bc8>, <Element div at 0x7f7e566c9808>, <Element div at 0x7f7e566c9608>, <Element div at 0x7f7e566c9d48>, <Element div at 0x7f7e566c9088>, <Element div at 0x7f7e566be9c8>, <Element div at 0x7f7e566bee08>, <Element div at 0x7f7e566bedc8>, <Element div at 0x7f7e566bed88>, <Element div at 0x7f7e566beec8>, <Element div at 0x7f7e566bed48>, <Element div at 0x7f7e566befc8>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/2/
---html_object---
 <Element html at 0x7f7e59e30ac8>
---object_list---
 [<Element div at 0x7f7e55e409c8>, <Element div at 0x7f7e55e40e88>, <Element div at 0x7f7e566a9f88>, <Element div at 0x7f7e566be9c8>, <Element div at 0x7f7e566bed48>, <Element div at 0x7f7e566beec8>, <Element div at 0x7f7e566bedc8>, <Element div at 0x7f7e566bed88>, <Element div at 0x7f7e566bef48>, <Element div at 0x7f7e566bee88>, <Element div at 0x7f7e566bef88>, <Element div at 0x7f7e566c9148>, <Element div at 0x7f7e566c9e08>, <Element div at 0x7f7e566c9608>, <Element div at 0x7f7e566c9808>, <Element div at 0x7f7e566c9bc8>, <Element div at 0x7f7e566c9d88>, <Element div at 0x7f7e566c9548>, <Element div at 0x7f7e566c9688>, <Element div at 0x7f7e566c9508>, <Element div at 0x7f7e566c9ec8>, <Element div at 0x7f7e566c9fc8>, <Element div at 0x7f7e566c9f48>, <Element div at 0x7f7e566c9c88>, <Element div at 0x7f7e566c9048>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/3/
---html_object---
 <Element html at 0x7f7e572a7488>
---object_list---
 [<Element div at 0x7f7e572d0608>, <Element div at 0x7f7e572d0248>, <Element div at 0x7f7e572d0908>, <Element div at 0x7f7e572d0848>, <Element div at 0x7f7e55e1e948>, <Element div at 0x7f7e55e1eec8>, <Element div at 0x7f7e55e1eac8>, <Element div at 0x7f7e55e414c8>, <Element div at 0x7f7e55e41788>, <Element div at 0x7f7e55e28f08>, <Element div at 0x7f7e55e28808>, <Element div at 0x7f7e55e28e88>, <Element div at 0x7f7e55e28c88>, <Element div at 0x7f7e55e28608>, <Element div at 0x7f7e55e28d88>, <Element div at 0x7f7e55e28908>, <Element div at 0x7f7e566b7d48>, <Element div at 0x7f7e566b7948>, <Element div at 0x7f7e566b7a48>, <Element div at 0x7f7e566b7bc8>, <Element div at 0x7f7e566b7048>, <Element div at 0x7f7e566b77c8>, <Element div at 0x7f7e566b7908>, <Element div at 0x7f7e566b7708>, <Element div at 0x7f7e566b72c8>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/4/
---html_object---
 <Element html at 0x7f7e566bee08>
---object_list---
 [<Element div at 0x7f7e55e46988>, <Element div at 0x7f7e55e460c8>, <Element div at 0x7f7e55e46088>, <Element div at 0x7f7e55e46108>, <Element div at 0x7f7e55e46288>, <Element div at 0x7f7e55e46188>, <Element div at 0x7f7e55e461c8>, <Element div at 0x7f7e55e1e3c8>, <Element div at 0x7f7e55e1e748>, <Element div at 0x7f7e55e1eac8>, <Element div at 0x7f7e55e1ecc8>, <Element div at 0x7f7e55e1ee88>, <Element div at 0x7f7e55e1ee08>, <Element div at 0x7f7e55e1ebc8>, <Element div at 0x7f7e55e1e348>, <Element div at 0x7f7e55e1ed88>, <Element div at 0x7f7e55e1e108>, <Element div at 0x7f7e55e1e048>, <Element div at 0x7f7e55e1e248>, <Element div at 0x7f7e55e1ed08>, <Element div at 0x7f7e572d0848>, <Element div at 0x7f7e572d0648>, <Element div at 0x7f7e566a9d88>, <Element div at 0x7f7e566c9f88>, <Element div at 0x7f7e566c9b88>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/5/
---html_object---
 <Element html at 0x7f7e5810ed48>
---object_list---
 [<Element div at 0x7f7e55e3d2c8>, <Element div at 0x7f7e55e3d148>, <Element div at 0x7f7e55e3d108>, <Element div at 0x7f7e55e3d448>, <Element div at 0x7f7e55e3d608>, <Element div at 0x7f7e55e3d308>, <Element div at 0x7f7e55e3d0c8>, <Element div at 0x7f7e55e3da88>, <Element div at 0x7f7e55e3d688>, <Element div at 0x7f7e55e3d408>, <Element div at 0x7f7e55e3dec8>, <Element div at 0x7f7e55e3d9c8>, <Element div at 0x7f7e55e3d1c8>, <Element div at 0x7f7e5b808588>, <Element div at 0x7f7e5b808048>, <Element div at 0x7f7e5b808f88>, <Element div at 0x7f7e57358108>, <Element div at 0x7f7e5b7ffe88>, <Element div at 0x7f7e55e40f88>, <Element div at 0x7f7e55e40088>, <Element div at 0x7f7e55e40c48>, <Element div at 0x7f7e55e40188>, <Element div at 0x7f7e55e40288>, <Element div at 0x7f7e55e40488>, <Element div at 0x7f7e55e40208>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/6/
---html_object---
 <Element html at 0x7f7e572d2248>
---object_list---
 [<Element div at 0x7f7e55e49dc8>, <Element div at 0x7f7e55e49ec8>, <Element div at 0x7f7e5b811148>, <Element div at 0x7f7e55e47708>, <Element div at 0x7f7e55e47488>, <Element div at 0x7f7e55e47408>, <Element div at 0x7f7e55e47d88>, <Element div at 0x7f7e55e47388>, <Element div at 0x7f7e55e47308>, <Element div at 0x7f7e55e47588>, <Element div at 0x7f7e55e47b48>, <Element div at 0x7f7e55e473c8>, <Element div at 0x7f7e55e47088>, <Element div at 0x7f7e55e47888>, <Element div at 0x7f7e55e47bc8>, <Element div at 0x7f7e55e3dc88>, <Element div at 0x7f7e55e3d588>, <Element div at 0x7f7e55e3d8c8>, <Element div at 0x7f7e55e3da88>, <Element div at 0x7f7e55e3d608>, <Element div at 0x7f7e55e3da08>, <Element div at 0x7f7e55e3d9c8>, <Element div at 0x7f7e55e3dec8>, <Element div at 0x7f7e55e3d408>, <Element div at 0x7f7e55e3d308>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/7/
---html_object---
 <Element html at 0x7f7e55e411c8>
---object_list---
 [<Element div at 0x7f7e59e30ac8>, <Element div at 0x7f7e566c9f08>, <Element div at 0x7f7e566c9508>, <Element div at 0x7f7e566c91c8>, <Element div at 0x7f7e5b808f88>, <Element div at 0x7f7e55e46f08>, <Element div at 0x7f7e55e46fc8>, <Element div at 0x7f7e55e46088>, <Element div at 0x7f7e55e463c8>, <Element div at 0x7f7e55e462c8>, <Element div at 0x7f7e566b71c8>, <Element div at 0x7f7e566b7288>, <Element div at 0x7f7e566b77c8>, <Element div at 0x7f7e566b7508>, <Element div at 0x7f7e566b7b08>, <Element div at 0x7f7e566b7d08>, <Element div at 0x7f7e566b7088>, <Element div at 0x7f7e566b75c8>, <Element div at 0x7f7e566b7ac8>, <Element div at 0x7f7e566b7488>, <Element div at 0x7f7e566b7408>, <Element div at 0x7f7e55e28a88>, <Element div at 0x7f7e55e28a08>, <Element div at 0x7f7e55e28748>, <Element div at 0x7f7e55e28d08>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/8/
---html_object---
 <Element html at 0x7f7e5b7ffe88>
---object_list---
 [<Element div at 0x7f7e55e49088>, <Element div at 0x7f7e566c93c8>, <Element div at 0x7f7e566c91c8>, <Element div at 0x7f7e566c9208>, <Element div at 0x7f7e566c9ec8>, <Element div at 0x7f7e566c9f08>, <Element div at 0x7f7e566c9108>, <Element div at 0x7f7e566c9d88>, <Element div at 0x7f7e566c9e08>, <Element div at 0x7f7e566a9fc8>, <Element div at 0x7f7e566a9f88>, <Element div at 0x7f7e55e409c8>, <Element div at 0x7f7e55e406c8>, <Element div at 0x7f7e55e40d08>, <Element div at 0x7f7e55e40648>, <Element div at 0x7f7e59e30a08>, <Element div at 0x7f7e55e46e88>, <Element div at 0x7f7e55e461c8>, <Element div at 0x7f7e55e463c8>, <Element div at 0x7f7e55e462c8>, <Element div at 0x7f7e55e46d08>, <Element div at 0x7f7e55e46348>, <Element div at 0x7f7e55e46f08>, <Element div at 0x7f7e55e46088>, <Element div at 0x7f7e55e46fc8>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/9/
---html_object---
 <Element html at 0x7f7e55e1e948>
---object_list---
 [<Element div at 0x7f7e566befc8>, <Element div at 0x7f7e566bec48>, <Element div at 0x7f7e566bed48>, <Element div at 0x7f7e566bee08>, <Element div at 0x7f7e572d0988>, <Element div at 0x7f7e572d0848>, <Element div at 0x7f7e566b7848>, <Element div at 0x7f7e566b7608>, <Element div at 0x7f7e566b7748>, <Element div at 0x7f7e55e49288>, <Element div at 0x7f7e55e49c08>, <Element div at 0x7f7e55e49f88>, <Element div at 0x7f7e55e496c8>, <Element div at 0x7f7e55e49088>, <Element div at 0x7f7e55e49d08>, <Element div at 0x7f7e55e49988>, <Element div at 0x7f7e55e49ec8>, <Element div at 0x7f7e55e49a88>, <Element div at 0x7f7e55e49a08>, <Element div at 0x7f7e55e49d48>, <Element div at 0x7f7e55e49808>, <Element div at 0x7f7e55e49608>, <Element div at 0x7f7e55e49908>, <Element div at 0x7f7e55e49888>, <Element div at 0x7f7e55e49488>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/10/
---html_object---
 <Element html at 0x7f7e55e4f348>
---object_list---
 [<Element div at 0x7f7e55e4fac8>, <Element div at 0x7f7e55e4fa88>, <Element div at 0x7f7e55e4fbc8>, <Element div at 0x7f7e55e4f088>, <Element div at 0x7f7e55e4f188>, <Element div at 0x7f7e55e4f0c8>, <Element div at 0x7f7e55e4f208>, <Element div at 0x7f7e55e4f2c8>, <Element div at 0x7f7e55e4f4c8>, <Element div at 0x7f7e55e417c8>, <Element div at 0x7f7e55e41a48>, <Element div at 0x7f7e55e411c8>, <Element div at 0x7f7e5810ecc8>, <Element div at 0x7f7e5b808588>, <Element div at 0x7f7e5b808048>, <Element div at 0x7f7e55e3d448>, <Element div at 0x7f7e55e3de08>, <Element div at 0x7f7e55e3dac8>, <Element div at 0x7f7e55e3dc08>, <Element div at 0x7f7e55e3d388>, <Element div at 0x7f7e55e3d188>, <Element div at 0x7f7e55e3d7c8>, <Element div at 0x7f7e55e3d9c8>, <Element div at 0x7f7e55e3d408>, <Element div at 0x7f7e55e3d588>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/11/
---html_object---
 <Element html at 0x7f7e572d0608>
---object_list---
 [<Element div at 0x7f7e55e49048>, <Element div at 0x7f7e55e49108>, <Element div at 0x7f7e55e49b88>, <Element div at 0x7f7e55e49c88>, <Element div at 0x7f7e55e40348>, <Element div at 0x7f7e55e40a48>, <Element div at 0x7f7e55e40f88>, <Element div at 0x7f7e55e40648>, <Element div at 0x7f7e55e40bc8>, <Element div at 0x7f7e55e40d88>, <Element div at 0x7f7e55e404c8>, <Element div at 0x7f7e55e40988>, <Element div at 0x7f7e55e406c8>, <Element div at 0x7f7e55e40508>, <Element div at 0x7f7e55e40908>, <Element div at 0x7f7e55e1e808>, <Element div at 0x7f7e55e28a08>, <Element div at 0x7f7e55e28248>, <Element div at 0x7f7e55e286c8>, <Element div at 0x7f7e55e28cc8>, <Element div at 0x7f7e55e28c08>, <Element div at 0x7f7e55e28e48>, <Element div at 0x7f7e55e28f48>, <Element div at 0x7f7e55e28808>, <Element div at 0x7f7e55e28208>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/12/
---html_object---
 <Element html at 0x7f7e55e4f708>
---object_list---
 [<Element div at 0x7f7e566c9cc8>, <Element div at 0x7f7e566c94c8>, <Element div at 0x7f7e57358108>, <Element div at 0x7f7e55e501c8>, <Element div at 0x7f7e55e50f88>, <Element div at 0x7f7e55e50e88>, <Element div at 0x7f7e55e50ec8>, <Element div at 0x7f7e55e504c8>, <Element div at 0x7f7e55e50348>, <Element div at 0x7f7e566b7a48>, <Element div at 0x7f7e566b7d88>, <Element div at 0x7f7e566b7088>, <Element div at 0x7f7e566b7d48>, <Element div at 0x7f7e566b73c8>, <Element div at 0x7f7e566b7a08>, <Element div at 0x7f7e566b7988>, <Element div at 0x7f7e55e47308>, <Element div at 0x7f7e55e47c08>, <Element div at 0x7f7e55e47dc8>, <Element div at 0x7f7e55e47748>, <Element div at 0x7f7e55e47a48>, <Element div at 0x7f7e55e47488>, <Element div at 0x7f7e55e47e08>, <Element div at 0x7f7e55e47808>, <Element div at 0x7f7e55e47448>]
保存成功
正在解析： https://www.qiushibaike.com/hot/page/13/
---html_object---
 <Element html at 0x7f7e572d2e48>
---object_list---
 [<Element div at 0x7f7e55e28c48>, <Element div at 0x7f7e55e28e08>, <Element div at 0x7f7e55e4bfc8>, <Element div at 0x7f7e55e4be48>, <Element div at 0x7f7e55e4bf48>, <Element div at 0x7f7e55e4b7c8>, <Element div at 0x7f7e55e4b608>, <Element div at 0x7f7e55e4bbc8>, <Element div at 0x7f7e55e4bc48>, <Element div at 0x7f7e55e4bdc8>, <Element div at 0x7f7e55e4bd48>, <Element div at 0x7f7e55e4b648>, <Element div at 0x7f7e55e41a88>, <Element div at 0x7f7e55e41148>, <Element div at 0x7f7e55e41548>, <Element div at 0x7f7e55e41408>, <Element div at 0x7f7e55e41508>, <Element div at 0x7f7e566bed48>, <Element div at 0x7f7e566bee08>, <Element div at 0x7f7e566bef08>, <Element div at 0x7f7e55e40088>, <Element div at 0x7f7e55e40808>, <Element div at 0x7f7e55e40688>, <Element div at 0x7f7e55e40c88>, <Element div at 0x7f7e55e40cc8>]
保存成功
关闭文件

Process finished with exit code 0
"""
