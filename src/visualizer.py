import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import parseData
import seaborn as sns
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def accidentByHour(caractData, show_res = True):
    hours = []
    counts = [0] * 24
    for acc_id, data in caractData.items():
        h = int(data[3][:2])
        hours += [h]
        counts[h] += 1

    total_accidents = sum(counts)
    hour_weights = {h: (counts[h] / total_accidents) for h in range(24)}

    if show_res:
        plt.hist(hours, bins=24, edgecolor="black")
        plt.xlabel("Hour of the day")
        plt.ylabel("Number of accidents")
        plt.title("Number of accidents by hour")
        plt.show()
    
    return hour_weights

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

def severityByAtmos(caractData, usagersData, show_res = True):
    accidents = {}
    for acc_id, data in caractData.items():
        accidents[acc_id] = [data[9],usagersData[acc_id][5]] # Weather condition / Accident's severity

    plotData = {1: [0 for _ in range(9)],
                2: [0 for _ in range(9)],
                3: [0 for _ in range(9)],
                4: [0 for _ in range(9)]}



    for acc_id, data in accidents.items():
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

    if show_res:
        df_t.plot(kind='bar', stacked=True,
            title='Severity of accidents by weather conditions')
        plt.show()

    df_norm = df_t.div(df_t.sum(axis=1), axis=0) * 100 
    if show_res:
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

    if show_res:
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

    return df_deviation.to_dict(orient="index")

def accidentByDay(caractData, show_res = True):
    accidents_in_day = {}
    for acc_id, data in caractData.items():
        day = data[0] + "/" + data[1] + "/" + data[2]
        if day not in accidents_in_day:
            accidents_in_day[day] = 1
        else:
            accidents_in_day[day] += 1

    if show_res:
        sorted_keys = sorted(accidents_in_day.keys(), key=lambda x: datetime.strptime(x, "%d/%m/%Y"))
        counts = [accidents_in_day[k] for k in sorted_keys]

        plt.figure(figsize=(14, 6))
        plt.bar(sorted_keys, counts, color='teal', edgecolor='black')
        plt.title('Daily Car Accidents (Gap-Corrected)', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Number of Accidents', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

    return accidents_in_day

def plotAccidentsByYearStacked(caractData):
    yearly_groups = {}
    for acc_id, data in caractData.items():
        year = str(data[2])
        day_str = f"{str(data[0]).zfill(2)}/{str(data[1]).zfill(2)}/{year}"
        
        if year not in yearly_groups:
            yearly_groups[year] = {}
        yearly_groups[year][day_str] = yearly_groups[year].get(day_str, 0) + 1

    sorted_years = sorted(yearly_groups.keys())
    num_years = len(sorted_years)

    fig, axes = plt.subplots(nrows=num_years, ncols=1, figsize=(14, 3 * num_years), sharex=False)
    
    if num_years == 1:
        axes = [axes]

    for i, year in enumerate(sorted_years):
        ax = axes[i]
        year_dict = yearly_groups[year]
        
        start_date = datetime(int(year), 1, 1)
        end_date = datetime(int(year), 12, 31)
        
        plot_dates = []
        plot_counts = []
        
        curr = start_date
        while curr <= end_date:
            d_str = curr.strftime("%d/%m/%Y")
            plot_dates.append(curr)
            plot_counts.append(year_dict.get(d_str, 0))
            curr += timedelta(days=1)

        ax.plot(plot_dates, plot_counts, color='#2c7fb8', linewidth=1.2)
        ax.fill_between(plot_dates, plot_counts, color='#2c7fb8', alpha=0.1)
        
        ax.set_title(f"Year: {year}", loc='left', fontweight='bold', fontsize=12)
        ax.set_ylabel("Accidents")
        ax.grid(True, linestyle='--', alpha=0.5)
        
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    year_tuple = (2020,2024)
    caracDict = parseData.parseMultipleYears(year_tuple, "caract")
    usagersDict = parseData.parseMultipleYears(year_tuple, "usagers")
    # severityByAtmos(caracDict, usagersDict)
    # accidentByAtmos(caracDict)
    # accidentByHour(caracDict)
    # print(severityByAtmos(caracDict, usagersDict, False))
    # print(accidentByHour(caracDict, True))
    # print(accidentByDay(caracDict))
    print(plotAccidentsByYearStacked(caracDict))