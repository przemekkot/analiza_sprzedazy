import pandas as pd
import datetime as dt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash()
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


prod_cat_info = pd.read_csv(r'db\prod_cat_info.csv')
country_codes = pd.read_csv(r'db\country_codes.csv', index_col=0)
customers = pd.read_csv(r'db\customers.csv', index_col=0)
tran_2016 = pd.read_csv(r'db\transactions\transactions-2016.csv', index_col=0).reset_index().drop(columns='index')
tran_2017 = pd.read_csv(r'db\transactions\transactions-2017.csv', index_col=0).reset_index().drop(columns='index')
tran_2018 = pd.read_csv(r'db\transactions\transactions-2018.csv', index_col=0).reset_index().drop(columns='index')
tran_2019 = pd.read_csv(r'db\transactions\transactions-2019.csv', index_col=0).reset_index().drop(columns='index')
transactions = pd.concat([tran_2016, tran_2017, tran_2018, tran_2019], axis=0)
transactions.merge(prod_cat_info, on='prod_cat_code', how='left')
pd.merge(transactions, customers, how='left', left_on='cust_id', right_on='customer_Id')
transactions['tran_date'] = pd.to_datetime(transactions['tran_date'])
transactions['day_of_week'] = transactions['tran_date'].dt.day_name()
df=transactions


grouped = df[df['total_amt']>0].groupby(['Store_type'])['total_amt'].sum()
fig = go.Figure(data=[go.Bar(x=grouped.index,y=grouped.values)],layout=[go.Layout(title='Udział klientów ze względy na płeć w poszczególnych kanałach sprzedaży')])
    
layout = html.Div(children=[html.H1('Kanały sprzedaży',style={'text-align':'center'}),

                        html.Div([dcc.Graph(id='bar-store-type',figure=fig)],style={'width':'50%'}),
                        html.Div(id='temp-out')
                        ])    



if __name__ == '__main__':
    app.run_server(debug=True)