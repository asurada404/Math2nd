# coding=UTF-8
import re
import time
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree
import traceback
def cleanData(filename):
    with open(filename,'r') as f:
        html = f.read()
        # print html
        selector = etree.HTML(html)
        #zheng ge de div
        idList = selector.xpath("//div[@class='list_con']/div[@class='WB_text']/a[1]/@href")
        commentList = selector.xpath("//div[@class='list_con']/div[@class='WB_text']/span")
        forwardNumList = selector.xpath("//div[@class='list_con']/div[@class='WB_func clearfix']/div[@class='WB_handle W_fr']/ul/li[2]/span/a")
        urlList = selector.xpath("//div[@class='list_con']/div[@class='WB_func clearfix']/div[@class='WB_from S_txt2']/a")

        print 'id:',idList[1]
        print 'comment:',commentList[1].text
        print 'forwardNum:',forwardNumList[3].text[-1]
        forwardContent = forwardNumList[3].text[-1]
        if forwardContent.isdigit():
            forwardNum = forwardContent
        else:
            forwardNum =0
        print 'forwardNum:', forwardNum
        print 'url:','http://weibo.com'+urlList[1].attrib['href']
        print 'time:' ,urlList[1].attrib['title']


cleanData('data2.html')