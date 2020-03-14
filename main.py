"""
Goal: Parse president from dataset and pritn information about them
"""


import csv
import President


def main():
    with open("C:\\Users\\Preston\\PycharmProjects\\gpaPresProj\\assets\\us_presidents.csv") as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            if count == 0:
                pass
            else:
                curPres = President.President(row)
                print(curPres)
            count += 1
main()