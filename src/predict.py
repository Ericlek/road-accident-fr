import pandas as pd

class AccidentPredict:
    def __init__(self, hours_weight, deviation_mean):
        self.hours_weight = hours_weight
        self.deviation_mean = deviation_mean
    
    def predict_day(self, forecast):
        """
        Docstring for predict_day
        
        :param self: Predicts the number of accident and their severity based on the 24H forecast
        :param forecast: Array of 24 elements representing a given weather for each hour of the day
        """
        predicted_accident = 0
        predicted_severity = {"Hospitalized": 0, "Dead": 0}

        for hour, weather in enumerate(forecast):
            prob_h = self.hours_weight.get(hour)
            estimated_accidents = daily_avg * prob_h