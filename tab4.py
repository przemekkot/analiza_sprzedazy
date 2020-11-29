import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('Store_type')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział klientów ze względy na płeć w poszczególnych kanałach sprzedaży'))

    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-store-type-test',figure=fig)],style={'width':'50%'}), # id do zmiany ? / zmienione ale czy trzeba?
                        html.Div([dcc.Dropdown(id='store_type_dropdown-test', 
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='bar-store-type-test')],style={'width':'50%'})],style={'display':'flex'}), 
                                    html.Div(id='temp-out') # id do zmiany ?
                        ])

    return layout