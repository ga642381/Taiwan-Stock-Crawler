from Crawler import Crawler_CSV
from dataBaseManager import dataBaseManager
#fname : 'wanted','Taiwan-50','Taiwan-Dividend'
fname = 'Taiwan-Dividend'
fnames = ['Taiwan-50','Taiwan-Dividend']


if __name__ == '__main__': 
    for fname in fnames:
        Crawler_CSV = Crawler_CSV(fname)        
        Crawler_CSV.craw()
        
        '''
        dataBaseManager = dataBaseManager()
        dataBaseManager.mergeCSV(fname)
        dataBaseManager.cleanData(fname)
        '''