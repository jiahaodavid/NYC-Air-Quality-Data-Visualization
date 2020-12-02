import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statistics
from datetime import datetime

#read the dataset
df = pd.read_csv('https://rcung000.github.io/ad_viz_plotval_data_modified.csv')

#additional details for coloring
colors = ['rgb(255,0,0)','rgb(255,127,0)','rgb(255,255,0)','rgb(127,255,0)',
          'rgb(0,255,0)','rgb(0,255,127)','rgb(0,255,255)','rgb(0,127,255)',
          'rgb(0,0,225)','rgb(127,0,255)','rgb(255,0,255)','rgb(255,0,127)']
months = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'June',7:'July',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
monthNum = [1,2,3,4,5,6,7,8,9,10,11,12]
countyParse = ['NULL','Albany','Bronx','Erie','Monroe','New York','Queens','Steuben']

def graph_2_1():
    fig = go.Figure()

    #sort by county and then by month
    for i in range(0,8):
        df_county = df.loc[df['COUNTY'] == (countyParse[i])]
        for j in range(1,13)[::1]:
            df_month = df_county.query('Month == %d' % i)
            fig.add_trace(go.Scattergeo(
                    lon = df_month['SITE_LONGITUDE'],
                    lat = df_month['SITE_LATITUDE'],
                    text = df_month['Daily Max 8-hour CO Concentration'].mean(),
                    name = countyParse[i] + months[j],
                    marker = dict(
                        size = df_month['Daily Max 8-hour CO Concentration']*100,
                        color = colors[j-1],
                        opacity = 0.5,
                        line_width = 0,
                        sizemode = 'area'
                    )))

    fig.update_layout(
            title_text = 'NYC 2019 Air Quality',
            showlegend = True,
            geo = dict(
                scope = 'usa',
                landcolor = 'rgb(217, 217, 217)',
            )
        )

    fig.update_geos(fitbounds='locations')

    return fig