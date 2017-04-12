
import random
def getIp(self):
    ipList = []
    with open('ipList.txt','r') as f:
        for line in f.readlines():
            ipList.append('http://'+line.strip())
    proxy_ip = random.choice(ipList)
    proxies = {'http': proxy_ip}
    return proxies

# 不使用代理代打开ip138
browser=webdriver.PhantomJS(PATH_PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='1.9.171.51:800'
# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000

proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())

# 还原为系统代理
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.DIRECT
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')