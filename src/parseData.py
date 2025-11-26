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

def parseLieux(year):
    year = str(year)
    file = 'lieux-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='|')
        for row in caracreader:
            print(', '.join(row))

def parseUsagers(year):
    year = str(year)
    file = 'usagers-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='|')
        for row in caracreader:
            print(', '.join(row))

def parseVehicules(year):
    year = str(year)
    file = 'vehicules-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='|')
        for row in caracreader:
            print(', '.join(row))

if __name__ == "__main__":
    parseLieux(2024)
    