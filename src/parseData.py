import os
import csv

def parseCaract(year):
    year = str(year)
    file = 'caract-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    print(path)
    with open(file=path):
        pass


if __name__ == "__main__":
    parseCaract(2024)
    