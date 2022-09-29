from datetime import datetime

class BetterDate:    
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
    
    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)
        
today = datetime.today()
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)
bd2 = BetterDate.from_datetime(today)
print(bd2.year)
print(bd2.month)
print(bd2.day)