# Taiwan Stock Crawler
Taiwan Stock Crawler is a crawler which directly crawl the data from [臺灣證券交易所（TWSE）](http://www.twse.com.tw). The historical trading information of individual securities will be downloaded in .csv format. The data can be used to analyze and visualize with ELK stack ( plaese see the project [ELK-Stack](https://github.com/ga642381/ELK-Stack) ).

## Data Description
The crawled csv file include daily inforamtion : 'Date', 'Trade Volume', 'Trade Value', 'Opening Price', 'Highest Price', 'Lowest Price', 'Closing Price ', 'Change', 'Transaction' of individual securities in past few years. 

＊『個股日成交資訊』以CSV檔儲存，包含：「日期」、「成交股數」、「成交金額」、「開盤價」、「最高價」、「收盤價」、「漲跌價差」、「成交筆數」

## Get Started

修改config.ini ( 預設為爬取2010年1月至今「台灣50(0050)」的50支成份股之「個股日成交資訊」)

 ```bash 
 python main.py 
 ```
 ![image](https://github.com/ga642381/Taiwan-Stock-Crawler/blob/master/github_material/main.gif?raw=true)<br>
資料將儲存在stockCSV資料夾下,有每個月份的CSV檔,最後每支股票也會有一個合併後的歷史資料,儲存在ALL資料夾內。


## Config File (config.ini)

目前可以爬以下三種個股資訊：
* 'custom'          :  使用者自訂
* 'Taiwan-50'       :  元大台灣50(0050)的50支成份股
* 'Taiwan-Dividend' :  元大高股息(0056)的30支成份股


### Configuration:

[USER]
* OPTION    -> custom, Taiwan-50, Taiwan-Dividend （可選擇一項或多項,以逗號（,）隔開）
* CUSTOM    -> 若OPTION有選custom,在這個欄位輸入欲爬取的股票代號（以逗號（,）隔開）
* STARTYEAR -> 開始爬取的年份
* STARTMONTH-> 開始爬取的月份
