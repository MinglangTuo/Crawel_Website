# This is a sample Python script.
import requests
import re
from selenium import webdriver

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class crawel_data():
    def __init__(self):
        self.reflist = []

        self.headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Origin": "https://cqyt.eip.cnpc",
        'Referer': 'https://cqyt.eip.cnpc/sites/d1cyc/pages/index.html?siteUrl=/sites/d1cyc/news:tzgg"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36",
        "sec-ch-ua": "Not-A.Brand","v":"24, Chromium","v":"14",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
        }

        self.data = {
        'newsNumber': '999999999',
        'pageSize': '20',
        'pageIndex': '1',
        'subChannelNumber': '0',
        'NewsSiteJson':'[{"paramenterlist":[{"ApplcationName":"https://cqyt.eip.cnpc/sites/d1cyc/news","ColumnEnName":"tzgg"}]}]'
        }


    def change_page(self):
        #改页数
        self.data['pageIndex'] = str(int(self.data['pageIndex'])+1)



    def findKeyPoint(self,text,keypoint):
        #查找关键词
        text_ = text.encode("utf8")
        pattern=r"HeadTitle\":\"[^\"]*"+keypoint+r".*?aspx"
        pattern_=pattern.encode("utf8")
        #pattern = keypoint
        results = re.findall(pattern_,text_)
        for i in range(len(results)):
            string__ = results[i].decode("utf8")
            strings_=string__.split("https")
            strings = "https"+strings_[1]
            if '</span>' not in string__:
                self.reflist.append(strings)
                print(strings)
        return results

    def get_brower(self,list,path):
        #启动浏览器
        driver = webdriver.Chrome(path)
        #r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        for posts in range(len(list)):
            driver.get(list[posts])
            if(posts!=len(list)-1):
                driver.execute_script("window.open('');")
                chwd = driver.window_handles
                driver.switch_to.window(chwd[-1])


    def requests_(self,keyvalue,page):
        #爬虫爬取
        for i in range(int(page)):
            response = requests.post('https://pfwebpart.eip.cnpc/EIP.WebPart.API/api/SreachNews/GetNewDataForPage',headers=self.headers, data=self.data, verify=False)
            self.findKeyPoint(response.text, keyvalue)
            self.change_page()




# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
