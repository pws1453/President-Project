"""
Class that provides information for president based off data from table
"""

import datetime


class President:
    def __init__(self, line):
        self.presNum = line[1]
        self.dateStart = self.datetimeDate(line[2])
        self.dateEnd = self.datetimeDate(line[3])
        self.name = line[4]
        self.prevPos = line[5]
        self.Polparty = line[6]
        self.vicePres = line[7]
        self.terms = self.termLength()

    def datetimeDate(self, date):
        return datetime.datetime.strptime(date, "%B %d, %Y")

    def termLength(self):
        if self.name == "Donald Trump":
            return 1
        timeSecs = self.dateEnd - self.dateStart
        tdays = timeSecs.days
        if tdays > ((365 * 12) + 10):
            return 4
        elif tdays > ((365 * 8) + 10):
            return 3
        elif tdays > ((365 * 4) + 10):
            return 2
        else:
            return 1

    def __str__(self):
        return f"President {self.presNum} was {self.name}." \
               f"Their party association was {self.Polparty}" \
               f"Before they were Presdient, they were the {self.prevPos}" \
               f"Their Vice President was {self.vicePres}" \
               f"They served {str(self.terms)} terms."