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
        self.termLength =
    def datetimeDate(self,date):
        return datetime.datetime.strptime(date,"%B %d, %Y")
    def termLength(self):
