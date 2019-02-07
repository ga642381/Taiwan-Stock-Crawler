from CrawlCSV import Crawler
fname = 'Taiwan Dividend'

if __name__ == '__main__':
    print('*Crawl : ', fname)    
    Crawler = Crawler()    
    #fname elf.stockCodeListDic = {'wanted':[],'Taiwan 50':[],'Taiwan Dividend':[]}
    Crawler.craw(fname)