import matplotlib.pyplot as plt
import numpy as np
import parseData

def accidentByHour(caractData):
    hours = []
    for acc_id, data in caractData.items():
        hours += [int(data[3][:2])]

    plt.hist(hours, bins=24, edgecolor="black")
    plt.xlabel("Heure de la journée")
    plt.ylabel("Nombre d'accidents")
    plt.title("Nombre d'accidents en fonction de l'heure")
    plt.show()

# Not meaningful
def accidentByAtmos(caractData):
    atmo = []
    for acc_id, data in caractData.items():
        atmo += [int(data[9])]
    atmo = [x for x in atmo if x != -1]
    plt.hist(atmo, bins = 10)
    plt.show()

if __name__ == "__main__":
    caracDict = parseData.parseCaract(2024)
    accidentByAtmos(caracDict)
    # accidentByHour(caracDict)