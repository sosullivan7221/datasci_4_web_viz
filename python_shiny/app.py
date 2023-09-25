# Packages
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, render, ui

# Load data
def load_data():
    path = '/home/sean_osullivan/datasci_4_web_viz/dataset/massachusetts_data.csv'
    return pd.read_csv(path)

df = load_data()
df_sleep = df[(df['MeasureId'] == 'SLEEP') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]



