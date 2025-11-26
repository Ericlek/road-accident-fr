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


if __name__ == "__main__":
    caracDict = parseData.parseCaract(2024)
    accidentByHour(caracDict)