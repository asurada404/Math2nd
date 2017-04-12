
from lxml import etree
def getHtmlData(filename):
    print 'kaishi %s de chuli '%filename
    with open(filename) as f:
        content = f.read()
        x = 'dkasld'
        content_replace =  content.replace('&lt;','<').replace('&gt;','>').replace('&amp;','&')
        #print content_replace
        html_head = '<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>Title</title></head><body>'
        html_end = '</body></html>'
        html_wanzheng = html_head + content_replace +html_end
        #print html_wanzheng

        selector = etree.HTML(html_wanzheng)
        forawrd_url_element = selector.xpath("//div[@class='WB_from S_txt2']/a/@href")

        for ele in forawrd_url_element:
            print ele
        #print forawrd_url

filenameList = []
for filename in filenameList:
    getHtmlData(filename)
    