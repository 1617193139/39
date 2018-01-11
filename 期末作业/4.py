# coding=gbk
import urllib
import urllib2
import re
import  thread
import time

class QCWY:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
        self.headers = {'User-Agent' :self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.gsrcw.com/job/?JobType=0&WorkPlace=0&Trade=0&Property=0&JobProperty=0&Degree=0&WorkYears=0&JobTag=0&Weal=0&MonthPay=0&PublishDate=0&Key=&Orderid=0&Styleid=2&PageNo=1' + str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "error",e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "page load error"
            return None
        pattern = re.compile('<li class="seaList12">.*?<a.*?>(.*?)</a>.*?<li class="seaList13">.*?<a.*?>(.*?)</a>.*?<li class="seaList14">.*?<span.*?>(.*?)</span>.*?<li class="seaList15">.*?(.*?)</li>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
           
       
            print u"\t职位：%s\t 工资：%s\n%s" %(story[0],story[2],story[1])

    def start(self):
        print u'正在读取，回车查看'
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage +=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QCWY()
spider.start()
