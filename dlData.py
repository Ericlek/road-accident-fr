import os
from urllib.request import urlopen, urlretrieve

yearLinks = {2024 : ["20251107-100210/2024.csv", "20251021-115900/caract-2024.csv", "20251021-115812/lieux-2024.csv", "20251021-115506/usagers-2024.csv"],
             2023 : ["20241023-153219/lieux-2023.csv", "20241028-103125/caract-2023.csv", "20241023-153253/vehicules-2023.csv", "20241023-153328/usagers-2023.csv"],
             2022 : ["20231005-094229/usagers-2022.csv", "20231005-094147/vehicules-2022.csv", "20231005-094112/lieux-2022.csv", "20231005-093927/carcteristiques-2022.csv"],
             2021 : ["20231009-140337/usagers-2021.csv", "20221024-113925/vehicules-2021.csv", "20221024-113901/lieux-2021.csv", "20221024-113743/carcteristiques-2021.csv"],
             2020 : ["20211110-111817/usagers-2020.csv", "20211110-111722/vehicules-2020.csv", "20211110-111603/lieux-2020.csv", "20211110-111202/caracteristiques-2020.csv"],}


urlBase = {2024 : "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024/",
           2023 : "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2023/",
           2022 : "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2021/",
           2021 : "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/",
           2020 : "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/"}

def exceptionLink(year, link):
    if year == 2021:
        if "usagers" in link:
            return "https://static.data.gouv.fr/resources/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/" + link
    else:
        return None

def download_csv(year, link):
    url = exceptionLink(year, link)
    if not url:
        url = urlBase[year] + link
    
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