import os
import csv

def parseCaract(year):
    year = str(year)
    file = 'caract-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='|')
        for row in caracreader:
            print(', '.join(row))


if __name__ == "__main__":
    parseCaract(2024)
    