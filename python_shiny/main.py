# Packages
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, render, ui

# Load data
def load_data():
    path = r'C:\Users\Sean\LocalDocuments\Code\AHI\datasci_4_web_viz\dataset\massachusetts_data.csv'
    return pd.read_csv(path)
df = load_data()
df_sleep = df[(df['MeasureId'] == 'SLEEP') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]

counties = df_sleep['LocationName'].unique()

# App

app_ui = ui.page_fluid(
    ui.input_select("county", "Select County", {county: county for county in counties}),
    ui.output_text_verbatim("avg_data_value"),
    ui.output_plot("bar_chart")
    )

def server(input, output, session):

    @output
    @render.text
    def avg_data_value():
        selected_county = input.county()
        avg_value = df_sleep[df_sleep['LocationName'] == selected_county]['Data_Value'].mean()
        return f"Adults Sleeping Less than 7 Hours Nightly Age-adjusted Prevalence for {selected_county}: {avg_value:.2f}%"

    @output
    @render.plot(alt="Adults Sleeping Less than 7 Hours Nightly Age-adjusted Prevalence Bar Chart")
    def bar_chart():
        overall_avg = df_sleep['Data_Value'].mean()
        selected_county_avg = df_sleep[df_sleep['LocationName'] == input.county()]['Data_Value'].mean()

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(['Selected County', 'Overall Average'], [selected_county_avg, overall_avg], color=['lightcoral', 'dodgerblue'])
        
        ax.set_ylabel('Data Value (Age-adjusted prevalence) - Percent')
        ax.set_ylim(0, 45)
        ax.set_title('Adults Sleeping Less than 7 Hours Nightly Age-adjusted Prevalence Comparison')
        
        return fig

app = App(app_ui, server)