# -*- coding:utf-8 -*-


import re
import urllib
import urllib2

from bs4 import BeautifulSoup



seed_url="http://www.jdlingyu.moe/tag/绝对领域/page/%s"


def  get_urls(new_url):
    #直接请求，首先使用urllib2进行网页的下载
    response = urllib2.urlopen(new_url)
    #获取状态码，如果是200说明成功获取网页
    #print response.getcode()
    #读取内容
    cont = response.read()
    #print cont
    
    #------------------------------------------------
    #使用beautifulsoup对网页进行解析
    #创建beautifulsoup对象
    soup = BeautifulSoup(cont,'html.parser',from_encoding='utf8')
    #print soup
    #查找所有标签img，链接"http://www.jdlingyu.moe/wp-content/uploads/thumbnail/"
    urls=soup.find_all('img',original=re.compile(r'.+?\.jpg'))
    return urls


def download_img(name,urls):
    
    for url in urls:
        #print url['original'] 打印图片url
        
        urllib.urlretrieve(url['original'],'F:\jd_ly\%s.jpg' % name)
        #使用urllib中的urlretrieve（）函数下载图片至设置好的文件路径，注意写文件名
        name += 1
    



#http://www.jdlingyu.moe/page/3/
page_size=1;
name=1;
while page_size!=37:
    new_url=seed_url % page_size
    urls=get_urls(new_url)#获取图片URL
    if name<325:
        download_img(name,urls)#下载图片至指定文件夹 
        
    page_size+=1
    name+=9


