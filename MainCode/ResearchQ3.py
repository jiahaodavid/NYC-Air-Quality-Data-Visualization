from configparser import ConfigParser
import pandas as pd
import plotly.graph_objects as go

configur = ConfigParser()
configur.read('config.ini')
mapbox_key = configur.get('mapbox', 'secret_token')

DataSet_Path = "https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/NYC/2019_outdoor_air_quality_NJ_NY.csv"

df = pd.read_csv(DataSet_Path)

ModData = df.groupby('Site Name').agg(
    {'Daily Mean PM2.5 Concentration': 'mean', 'SITE_LATITUDE': 'median', 'SITE_LONGITUDE': 'median'}).reset_index()

ModData = ModData.rename(columns={'Site Name': 'Locations', "Daily Mean PM2.5 Concentration": "AvgConcentration"})

site_lat = ModData.SITE_LATITUDE
site_lon = ModData.SITE_LONGITUDE
PM = ModData.AvgConcentration
locations_name = ModData.Locations

def graph_3_1():
    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=PM,
            showscale=True,
            colorbar={'title': 'Avg of PM2.5 Concentration', 'titleside': 'top', 'thickness': 4, 'ticksuffix': ' ug/m3'}
        ),
        text=locations_name,
        hoverinfo='text'
    ))

    fig.update_layout(
        title='2019 Avg PM2.5 Concentration in NYC',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=mapbox_key,
            bearing=0,
            center=dict(
                lat=40.7730,
                lon=-73.8702
            ),
            pitch=0,
            zoom=11,
            style='light'
        ),
    )

    return fig