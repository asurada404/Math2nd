# coding=utf-8
from selenium import webdriver
import re
import time
import string
import sys
import os
from bs4 import BeautifulSoup
from lxml import etree
import traceback
import json

def get_date(url,pageNum):
    print 'jinru pachong '
    #这个地方可以设置 header, 代理等一些参数
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    cap["phantomjs.page.settings.resourceTimeout"] = 1000
    cap["phantomjs.page.settings.loadImages"] = False
    cap["phantomjs.page.settings.disk-cache"] = True
    cap["phantomjs.page.customHeaders.Cookie"] = "SINAGLOBAL=2360215761240.332.1491479659323; wb_publish_fist100_3627866191=1; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-V5-G0=694581d81c495bd4b6d62b3ba4f9f1c8; _s_tentry=login.sina.com.cn; Apache=4580779082280.715.1491623615309; ULV=1491623615379:3:3:3:4580779082280.715.1491623615309:1491528041550; YF-Page-G0=23b9d9eac864b0d725a27007679967df; TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; TC-V5-G0=c427b4f7dad4c026ba2b0431d93d839e; TC-Page-G0=42b289d444da48cb9b2b9033b1f878d9; UM_distinctid=15b552021457a3-0781d56c232d15-317d0258-100200-15b552021461061; login_sid_t=7c7716d1a4c5292c82fedd2d5dc464f2; appkey=; WB_register_version=a05309c5d15974a8; WBtopGlobal_register_version=a05309c5d15974a8; SSOLoginState=1491834302; un=799746409@qq.com; wvr=6; SCF=AkFOQV_YX86QYO9wv_cZIfkPMxH16QkPRjbNirmrM_5J6JTChNwYNmbMOqvZiyrkjFqHtmgiBVB8M7kz122EWAQ.; SUB=_2A2516QpaDeThGeVI6VUZ9ijNwj2IHXVWn3ySrDV8PUNbmtBeLXLykW8dB5m8zVcxyX_BoDwBE2O7w2jlpA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh3gbx._VGZ0gCdq0DLHESW5JpX5KMhUgL.FoeceoMRSoqp1K22dJLoIEBLxK-L12-LBKnLxK-LB-BL1K5LxKqLBoMLBK2LxKqLBoMLBK2t; SUHB=00x5eOva3sxoUk; ALF=1523494282; UOR=,,login.sina.com.cn"
    # browser = webdriver.PhantomJS(desired_capabilities=cap)

    driver = webdriver.PhantomJS(executable_path="/home/ub/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs", desired_capabilities=cap)
    time.sleep(1)
    driver.set_window_size(1120, 1000)
    driver.get(url)
    page = driver.page_source
    # print data
    print 'get %d data'%pageNum
    print '========'
    rc = re.compile("\<.*?\>")
    re_page = rc.sub('', page)
    # json bianma
    res = json.loads(re_page)
    #tiqu  json zhong de data
    page_json_data = res['data']
    # data jinxing json bianma
    html = page_json_data['html']
    html = html.encode("utf-8")
    with open('./testdata/%d.txt'%pageNum,'w+') as f:
        f.write(html)
        f.close()
    print 'wancheng %d de  paqu'%pageNum

pageNum = 1
for i in range(1,173):
    pageNum = pageNum + 1

    url = 'http://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4095621185127112&max_id=4095741058588501&page=%d&__rnd=1491984246348'%pageNum

    get_date(url,pageNum)

    time.sleep(5)


