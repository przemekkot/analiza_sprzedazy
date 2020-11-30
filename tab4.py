import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('Store_type')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział kanałów sprzedaży w ogólnej sprzedaży'))

    layout = html.Div([html.H1('Kanały sprzedaży II',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='other-pie-store-type-two',figure=fig)],style={'width':'50%'}), 
                        html.Div([dcc.Dropdown(id='store_type_dropdown-two', 
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-store-type-two')],style={'width':'50%'})],style={'display':'flex'}), 
                                    html.Div(id='temp-out') 
                        ])

    return layout