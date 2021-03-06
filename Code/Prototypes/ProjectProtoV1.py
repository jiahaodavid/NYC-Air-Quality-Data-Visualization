import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

#creating the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#getting the data
urban_data = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Urban-Data/nyc_census_tracts.csv?token=ALH7XZLXZKEMDNYHI22SQHC7XPXXC')
queens = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/Queens/annual_36_081_0125_2017.csv?token=ALH7XZKN2EMEANS35D5O4UK7XPYBS')
brooklyn = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/Brooklyn/annual_36_047_0122_2017.csv?token=ALH7XZKZJD7JCNNKED4Y2RC7XPX7U')
bronx = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/Bronx/annual_36_005_0133_2017.csv?token=ALH7XZJ442RIAWAI5ZR5KVC7XPX6C')
staten_island = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/Staten%20Island/annual_36_085_0055_2017.csv?token=ALH7XZOH5Z2Q7PPHBUU6E3S7XPYDS')
manhattan = pd.read_csv('https://raw.githubusercontent.com/tislam35/Human-Perception-Project/main/Data/Air-Quality-Data/Manhattan/annual_36_061_0134_2017.csv?token=ALH7XZNH5VG35QXZPOT5I227XPYFK')

#filtering the data
urban_pop = urban_data.loc[:, ['Borough', 'TotalPop']].values
urban_pop = pd.DataFrame(data=urban_pop, columns = ['Borough', 'Total Population'])
urban_inc = urban_data.loc[:, ['Borough', 'Income']].values
urban_inc = pd.DataFrame(data=urban_inc, columns = ['Borough', 'Average Income'])
urban_pop['Total Population'] = pd.to_numeric(urban_pop['Total Population'])
urban_inc['Average Income'] = pd.to_numeric(urban_inc['Average Income'])
urban_pop = urban_pop.groupby(['Borough'],as_index=False).sum()
urban_inc = urban_inc.groupby(['Borough'],as_index=False).mean()
queens_25 = queens[queens['Parameter Name'] == "PM2.5 - Local Conditions"]
queens_25_val = queens_25['Arithmetic Mean'].iloc[0]
brooklyn_25 = brooklyn[brooklyn['Parameter Name'] == "PM2.5 - Local Conditions"]
brooklyn_25_val = brooklyn_25['Arithmetic Mean'].iloc[0]
bronx_25 = bronx[bronx['Parameter Name'] == "PM2.5 - Local Conditions"]
bronx_25_val = bronx_25['Arithmetic Mean'].iloc[0]
staten_island_25 = staten_island[staten_island['Parameter Name'] == "PM2.5 - Local Conditions"]
staten_island_25_val = staten_island_25['Arithmetic Mean'].iloc[0]
manhattan_25 = manhattan[manhattan['Parameter Name'] == "PM2.5 - Local Conditions"]
manhattan_25_val = manhattan_25['Arithmetic Mean'].iloc[0]
air_quality_data = pd.DataFrame(np.array([['Bronx', bronx_25_val],
                                          ['Brooklyn', brooklyn_25_val],
                                          ['Manhattan', manhattan_25_val],
                                          ['Queens', queens_25_val],
                                          ['Staten Island', staten_island_25_val]]),
                                columns=['Borough', 'PM 2.5 ??g/m^3'])
research_q1_data = pd.merge(urban_pop, urban_inc, how='inner', on=['Borough'])
research_q1_data = pd.merge(research_q1_data, air_quality_data, how='inner', on=['Borough'])

#creating the figure
fig = px.scatter(research_q1_data, x="PM 2.5 ??g/m^3", y="Average Income",
                 size="Total Population", color="Borough",
                 log_x=True, size_max=100)

#updating layout with the figure
app.layout = html.Div([dcc.Graph(id='graph-with-slider', figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)