import os
import requests
import time
import random
from stockCode import stockCode
from stockURL import stockURL
from stockTime import stockTime

class Crawler():
    def __init__(self):
        #self.processNumber = 2        
        self.stockCSVBaseDir = './stockCSV'
        self.stockCode = stockCode()
        self.stockURL = stockURL()
        self.stockTime = stockTime()
        self.fname = ''
    
    def createUrlFiles(self):
        self.stockURL.writeURLs(self.fname)
    
    def downloadCSV(self):
        urlBaseDir = os.path.join(self.stockURL.stockUrlBaseDir,self.fname) 
        fileList = os.listdir(urlBaseDir)
        
        #./stockUrlBaseDir/fname/NNNN
        #./stockCSVBaseDir/fname/NNNN
        
        
        #create stockCSV basedir
        if not os.path.exists(self.stockCSVBaseDir):
            os.makedirs(self.stockCSVBaseDir)
            print('*dir : ',self.stockCSVBaseDir,'  has been created')
        
        #create folders for different stockCode in different fname
        for file in fileList:
            folderPath = os.path.join(self.stockCSVBaseDir,self.fname,file)
            if not os.path.exists(folderPath):
                os.makedirs(folderPath)
        
        #download CSV file from TWSE:        
        for file in fileList:
            fileUrlPath = os.path.join(urlBaseDir,file)
            with open(fileUrlPath,'r') as urlf:
                for line in urlf:
                    date = line[:8]
                    url = line[8:]
                    url = url.strip('\n')                    
                    
                    folder = os.path.join(self.stockCSVBaseDir,self.fname,file)
                    csvPath = os.path.join(folder,date+'.csv')                    
                    if not os.path.exists(csvPath):
                        response = requests.get(url) ####try to make a connection
                        with open(csvPath,'w') as f:
                            f.write(response.text)
                        print(file,':',date)
                        #sleepTime = random.uniform(5,10)
                        time.sleep(20)
        
    def craw(self,fname):
        self.fname = fname
        self.createUrlFiles()
        STOCKCODES = self.stockURL.stockCode.stockCodeListDic[fname]
        print('*following {} Stocks will be crawled'.format(len(STOCKCODES)))
        print(STOCKCODES,'\n')
        self.downloadCSV()

    