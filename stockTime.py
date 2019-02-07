import datetime


#get current time
NOW = datetime.datetime.now()
CURRENTYEAR = NOW.year
CURRENTMONTH = NOW.month


class stockTime():
    def __init__(self):
        self.dateList = []       
        #begining of the query time
        self.startYear = 2010
        self.startMonth = 1
        
        #end of the query time, default is 'so far'
        self.endYear = CURRENTYEAR       
        self.endMonth = CURRENTMONTH
        
        self.yearList = []
        self.monthListFull = []
        self.monthListPartial = []
        self.dayList = []
        
    def addYear(self):
        for year in range(self.startYear, self.endYear+1):
            self.yearList.append(str(year))
    
    def addMonth(self):
        for i in range(12):
            month = str(i+1)
            month = month.zfill(2)
            self.monthListFull.append(month)
            
        for i in range(self.endMonth):
            month = str(i+1)
            month = month.zfill(2)
            self.monthListPartial.append(month)
            
    def addDay(self):
        day = str(1)
        day = day.zfill(2)
        self.dayList.append(day)
    
    def addDate(self):
        self.addYear()
        self.addMonth()
        self.addDay()
        
        currentYear = str(CURRENTYEAR)
        currnetMonth = str(CURRENTMONTH).zfill(2)
        
        for year in self.yearList[:-1]:
            for month in self.monthListFull:
                for day in self.dayList:
                    self.dateList.append(year+month+day)
        
        for month in self.monthListPartial:
            self.dateList.append(currentYear+month+day)
        
    def getDateList(self):
        self.addDate()
        dateList = self.dateList
        return dateList