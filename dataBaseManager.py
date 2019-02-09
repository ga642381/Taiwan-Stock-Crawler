import os
import configparser
import re
config = configparser.ConfigParser()
config.read('config.ini')

class dataBaseManager():
    def __init__(self):
        self.stockCSVBaseDir = config['PATH']['STOCKCSV_BASEDIR']
    
    def mergeCSV(self,fname):        
        CSVFnameDir = os.path.join(self.stockCSVBaseDir,fname)
        
        
        allDir = os.path.join(CSVFnameDir,'ALL')
        if not os.path.exists(allDir):
            os.makedirs(allDir)        
        
        stockCodes = os.listdir(CSVFnameDir)
        stockCodes.remove('ALL')
        
        for stockCode in stockCodes:            
            historyCSVDir = os.path.join(CSVFnameDir,stockCode)
            allCSVPath = os.path.join(allDir,stockCode+'.csv')            
            with open(allCSVPath,'w') as F:                
                historyCSVs = os.listdir(historyCSVDir)
                historyCSVs.sort()
                
                gotFirstFile = False                 
                for historyCSV in historyCSVs :
                    historyCSVPath = os.path.join(historyCSVDir,historyCSV)
                    
                    if os.stat(historyCSVPath).st_size > 3 and (not gotFirstFile):
                        gotFirstFile  = True
                        with open(historyCSVPath,'r') as f:
                            lines = f.readlines()
                            filedLine = lines[1]
                            F.write(filedLine)
                            for line in lines:
                                dateExist = re.findall('[0-9]+\/[0-9]+\/[0-9]+',line)
                                if dateExist:
                                    F.write(line)
                                
                                
                    elif os.stat(historyCSVPath).st_size > 3 and gotFirstFile: 
                        with open(historyCSVPath,'r') as f:
                            lines = f.readlines()
                            for line in lines:
                                dateExist = re.findall('[0-9]+\/[0-9]+\/[0-9]+',line)
                                if dateExist:
                                    F.write(line)
        
        print('\n*All the csv files of each stock have been merged')
    
    def synchronizeDataset(self):
        pass
    def dailyUpdate(self):
        pass