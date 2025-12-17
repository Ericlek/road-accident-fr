import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import parseData
import seaborn as sns

def accidentByHour(caractData):
    hours = []
    for acc_id, data in caractData.items():
        hours += [int(data[3][:2])]

    plt.hist(hours, bins=24, edgecolor="black")
    plt.xlabel("Hour of the day")
    plt.ylabel("Number of accidents")
    plt.title("Number of accidents by hour")
    plt.show()

# Not meaningful
def accidentByAtmos(caractData):
    weather_counts = [0]*9  
    weather_labels = ["Normal", "Light rain", "Heavy rain", "Snow", "Fog",
                      "Heavy storm", "Dazzling light", "Cloudy", "Others"]

    for acc_id, data in caractData.items():
        weather = int(data[9]) - 1  
        weather_counts[weather] += 1

    total = sum(weather_counts)
    weather_percent = [count / total * 100 for count in weather_counts]

    plt.figure(figsize=(10,6))
    plt.bar(weather_labels, weather_percent, color="blue")
    plt.ylabel("Percentage of Accidents (%)")
    plt.title("Percentage of Accidents by Weather")
    plt.xticks(rotation=45)
    plt.tight_layout()
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
        print(acc_id)
        if int(data[1]) != -1:
            plotData[int(data[1])][int(data[0]) - 1] += 1
    
    df = pd.DataFrame({
        "Severity": ["Unharmed", "Light wounds", "Hospitalized", "Dead"],
        "Normal": [plotData[1][0], plotData[4][0], plotData[3][0], plotData[2][0]],
        "Light rain": [plotData[1][1], plotData[4][1], plotData[3][1], plotData[2][1]],
        "Heavy rain": [plotData[1][2], plotData[4][2], plotData[3][2], plotData[2][2]],
        "Snow": [plotData[1][3], plotData[4][3], plotData[3][3], plotData[2][3]],
        "Fog": [plotData[1][4], plotData[4][4], plotData[3][4], plotData[2][4]],
        "Heavy storm": [plotData[1][5], plotData[4][5], plotData[3][5], plotData[2][5]],
        "Dazzling light": [plotData[1][6], plotData[4][6], plotData[3][6], plotData[2][6]],
        "Cloudy": [plotData[1][7], plotData[4][7], plotData[3][7], plotData[2][7]],
        "Others": [plotData[1][8], plotData[4][8], plotData[3][8], plotData[2][8]],
    })
    
    df_t = df.set_index("Severity").T

    df_t.plot(kind='bar', stacked=True,
        title='Severity of accidents by weather conditions')
    plt.show()

    df_norm = df_t.div(df_t.sum(axis=1), axis=0) * 100 
    df_norm.plot(kind="bar", stacked=True, figsize=(10,6),
                 title="Severity of Accidents by Weather (Percentage)")
    plt.xlabel("Weather")
    plt.ylabel("Percentage of Accidents")
    plt.xticks(rotation=45)
    plt.legend(title="Severity")
    plt.tight_layout()
    plt.show()

    df_norm = df_t.div(df_t.sum(axis=1), axis=0) * 100
    df_deviation = df_norm - df_norm.mean(axis=0)


    plt.figure(figsize=(10,6))
    sns.heatmap(df_norm, annot=True, fmt=".1f", cmap="YlGnBu")
    plt.title("Heatmap of Accident Severity by Weather (Percentage)")
    plt.xlabel("Severity")
    plt.ylabel("Weather")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,6))
    sns.heatmap(df_deviation, annot=True, fmt=".1f", cmap="coolwarm", center=0)
    plt.title("Deviation from Mean Percentage of Each Severity by Weather")
    plt.xlabel("Severity")
    plt.ylabel("Weather")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    caracDict = parseData.parseCaract(2022)
    usagersDict = parseData.parseUsagers(2022)
    severityByAtmos(caracDict, usagersDict)
    accidentByAtmos(caracDict)
    # accidentByHour(caracDict)