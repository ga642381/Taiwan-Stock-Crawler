from Crawler import Crawler_CSV
fname = 'Taiwan Dividend'

if __name__ == '__main__':
    print('*Crawl : ', fname)    
    Crawler_CSV = Crawler_CSV()    
    #fname elf.stockCodeListDic = {'wanted':[],'Taiwan 50':[],'Taiwan Dividend':[]}
    Crawler_CSV.craw(fname)