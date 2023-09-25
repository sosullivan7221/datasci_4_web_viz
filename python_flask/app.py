# Packages
from flask import Flask, render_template, request
import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Dataset
path = 'file:///home/sean_osullivan/datasci_4_web_viz/dataset/massachusetts_data.csv'
df = pd.read_csv(path)
df_sleep = df[(df['MeasureId'] == 'SLEEP') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]

@app.route('/', methods =['GET', 'POST'])
def index():
    counties = sorted(df_sleep['LocationName'].unique())
    selected_county = request.form.get('county') or counties[0]

    img = create_plot(selected_county)

    return render_template("index.html", counties=counties, selected_county=selected_county, img=img)

def create_plot(county):
    overall_avg = df_sleep['Data_Value'].mean()
    selected_county_avg = df_sleep[df_sleep['LocationName'] == county]['Data_Value'].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(['Selected County', 'Overall Average'], [selected_county_avg, overall_avg], color=['lightcoral', 'dodgerblue'])
    ax.axhline(selected_county_avg, color='gray', linestyle='dashed', alpha=0.7)
    ax.set_ylabel('Data Value (Age-adjusted prevalence) - Percent')
    ax.set_ylim(0, 40)
    ax.set_title('Adults sleeping less than 7 hours nightly Age-adjusted Prevalence Comparison')

    # Convert to PNG
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)    