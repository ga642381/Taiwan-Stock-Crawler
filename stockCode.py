import os
import re
from lxml import etree 
import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

class stockCode():    
    def __init__(self):
        #dictionary {fname: list}
        self.stockCodeListDic = {'wanted':[],'Taiwan-50':[],'Taiwan-Dividend':[]}
        
        #create BaseDir
        self.stockCodeBaseDir = config['PATH']['STOCKCODE_BASEDIR']
        if not os.path.exists(self.stockCodeBaseDir):
            os.makedirs(self.stockCodeBaseDir)
            print('*dir : ',self.stockCodeBaseDir,'  has been created')
    
    def writeStockCodes(self,fname):    
        
        #get stockCodelist
        self.appendStockCode(fname)
        fnamePath = os.path.join(self.stockCodeBaseDir,fname)
        with open(fnamePath,'w') as f:
            for stockCode in self.stockCodeListDic[fname]:
                f.write(stockCode)
                f.write('\n')    
                
    def getStockCodeList(self,fname):  
        stockCodeList= self.stockCodeListDic[fname]
        return stockCodeList
        
        
    
    
    
    #One should manually add the wanted stock code to /stockCode/wanted file   
    #Taiwan 50          Stock Codes will be automatically crawled
    #Taiwan Dividend    Stock Codes will be automatically crawled
    def appendStockCode(self,fname):        
        #if there's no history data
        if not os.path.exists(os.path.join(self.stockCodeBaseDir,fname)):
            self.crawlStockCode(fname)
            #self.writeStockCodes(fname)      
            
        #if there's history data, directly get the stockCode from it
        else:
            path = os.path.join(self.stockCodeBaseDir,fname)             
            with open(path,'r') as f:
                for line in f:
                    line=line.strip('\n') #strip the EOL symbol
                    self.stockCodeListDic[fname].append(line)# add each stockCode to the list 
                
    def crawlStockCode(self,fname):        
        CODE = False
        if fname == 'Taiwan-50':
            CODE = '0050'
        elif fname =='Taiwan-Dividend':
            CODE = '0056'
        if not CODE: return
        
        
        #Crawl stockCodes from cnyes.com:
        url = 'http://www.cnyes.com/twstock/Etfingredient/{}.htm'.format(CODE)
        get_url = requests.get(url)
        tree = etree.fromstring(get_url.content, etree.HTMLParser())
        
        TabBx = tree.xpath('//div[@class="TabBx"]') #hrefList = tree.xpath('//div[@class="TabBx"]/div[@class="tab"]//a')
        TabBx = etree.tostring(TabBx[0],pretty_print=True, method="html").decode('utf-8')
        profileNNNN = re.findall('profile\/[0-9]*',TabBx)        
        for element in profileNNNN:
            self.stockCodeListDic[fname].append(element[-4:])            
        

    

            

        
    

