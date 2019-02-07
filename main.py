from Crawler import Crawler_CSV
#fname : 'wanted','Taiwan 50','Taiwan Dividend'
fname = 'Taiwan 50'

if __name__ == '__main__':           
    Crawler_CSV = Crawler_CSV(fname)        
    Crawler_CSV.craw()