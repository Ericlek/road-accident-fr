import matplotlib.pyplot as plt
import pandas as pd
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

def severityByAtmos(caractData, usagersData):
    accidents = {}
    for acc_id, data in caractData.items():
        accidents[acc_id] = [data[9],usagersData[acc_id][5]] # Weather condition / Accident's severity

    plotData = {1: [0 for _ in range(9)],
                2: [0 for _ in range(9)],
                3: [0 for _ in range(9)],
                4: [0 for _ in range(9)]}


    for acc_id, data in accidents.items():
        plotData[int(data[1])][int(data[0]) - 1] += 1
    print(plotData)

    df = pd.DataFrame([["Unharmed"] + plotData[1], ["Light wounds"] + plotData[4],
                       ["Hospitalized"] + plotData[3], ["Dead"] + plotData[2]],
                       columns=["Severity", "Normal", "Light rain", "Heavy rain", "Snow",
                                "Fog", "Heavy storm", "Dazzling light", "Cloudy", "Others"])

    df.plot(x='Severity', kind='bar', stacked=True,
        title='Severity of accidents by weather conditions')
    
    plt.show()

    # print(accidents)

if __name__ == "__main__":
    caracDict = parseData.parseCaract(2024)
    usagersDict = parseData.parseUsagers(2024)
    severityByAtmos(caracDict, usagersDict)
    accidentByAtmos(caracDict)
    # accidentByHour(caracDict)