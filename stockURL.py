import os
from stockTime import stockTime
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

class stockURL():
    def __init__(self):
        #get the data from TWSE
        self.url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=YYYYmmdd&stockNo=NNNN'
        self.urlList = []
        self.stockCodeList = []        

        self.stockTime = stockTime()
        self.stockUrlBaseDir = config['PATH']['STOCKURL_BASEDIR']
        
        
    def writeURLs(self,fname,stockCodeList):
        #create UrlBaseDir
        fnameUrlBaseDir = os.path.join(self.stockUrlBaseDir,fname)
        if not os.path.exists(fnameUrlBaseDir):
            os.makedirs(fnameUrlBaseDir)
            print('*dir : ',fnameUrlBaseDir,'  has been created')
        
        timeList = self.stockTime.getDateList() 
              
        for NNNN in stockCodeList:
            path = os.path.join(fnameUrlBaseDir,NNNN)
            with open(path,'w') as f:  
                for YYYYmmdd in timeList:
                    url = self.url
                    url = url.replace('YYYYmmdd',YYYYmmdd)
                    url = url.replace('NNNN',NNNN)
                    f.write(YYYYmmdd+url)
                    f.write('\n')
