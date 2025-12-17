import os
import csv

def parseCaract(year):
    caracts = {}
    year = str(year)
    file = 'caract-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        next(caracfile)
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='"')
        for row in caracreader:
            if row != []:
                caracts[row[0]] = row[1:len(row)]
    return caracts

def parseLieux(year):
    lieux = {}
    year = str(year)
    file = 'lieux-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        next(caracfile)
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='"')
        for row in caracreader:
            if row != []:
                lieux[row[0]] = row[1:len(row)]
    return lieux

def parseUsagers(year):
    usagers = {}
    year = str(year)
    file = 'usagers-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        next(caracfile)
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='"')
        for row in caracreader:
            if row != []:
                row[1] = row[1].replace("\xa0", "")
                row[2] = row[2].replace("\xa0", "")
                if int(year) > 2020:
                    usagers[row[0]] = row[1:len(row)]
                else:
                    row.insert(1, "")
                    usagers[row[0]] = row[1:len(row)]
            # break
    return usagers

def parseVehicules(year):
    vehicules = {}
    year = str(year)
    file = 'vehicules-'+year+'.csv'
    dir = os.path.dirname(__file__)
    path = os.path.normpath(os.path.join(dir,'..','data',year,file))
    with open(file=path, newline='') as caracfile:
        next(caracfile)
        caracreader = csv.reader(caracfile, delimiter=';', quotechar='"')
        for row in caracreader:
            if row != []:
                row[1] = row[1].replace("\xa0", "")
                vehicules[row[0]] = row[1:len(row)]
    return vehicules

def parseMultipleYears(years, type):
    """
    Year is a tuple with start year to end year included
    """
    start, end = years
    yearsArray = [i for i in range(start, end+1)]

    functions = {"caract": parseCaract, "lieux": parseLieux, "usagers": parseUsagers, "vehicules": parseVehicules}
    dictRet = {}

    for year in years:
        dictRet = dictRet | functions[type](year)
    
    return dictRet


if __name__ == "__main__":
    # res = parseUsagers(2020)
    # print(res)
    res = parseMultipleYears((2020,2020), "usagers")
    print(res)
    