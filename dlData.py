import os
from urllib.request import urlopen, urlretrieve
import requests
import cgi

yearLinks = {
             2023 : ["20241023-153219/lieux-2023.csv", "20241028-103125/caract-2023.csv", "20241023-153253/vehicules-2023.csv", "20241023-153328/usagers-2023.csv"]}

def download_csv(year, link):
    url = "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/" + link
    dir = os.path.dirname(__file__)
    filename = link.split("/")[-1]
    destFolder = os.path.normpath(os.path.join(dir,'data',str(year)))

    if not os.path.exists(destFolder):
        os.makedirs(destFolder)  

    urlretrieve(url, destFolder + "/" + filename)

def main():
    for year, links in yearLinks.items():
        for link in links:
            download_csv(year, link)
    
if __name__ == "__main__":
    main()