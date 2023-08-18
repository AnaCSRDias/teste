import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go
import base64


colors = {'background': '#F5CFF7','text':'#A939AD '}
df = pd.read_csv('wheels.csv')

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode('ascii'))


app.layout = html.Div([
    html.H1(children='Módulo de Felicidade', style={'textAlign':'center',
                                                'color':colors['text']}),

    html.Div([
        dcc.RadioItems(id = 'wheels',
                       options = [{'label':i, 'value':i} for i in df['wheels'].unique()],
                       value =1),
        html.Div(id = 'wheels-output'),
        html.Hr(style = {'borderColor':'magenta','borderHeight': "10vh"}),
        dcc.RadioItems(id = 'colors',
                       options = [{'label':i, 'value':i} for i in df['color'].unique()],
                       value ='blue'),
        html.Div(id = 'colors-output'),
        html.Img(id = 'display-image',src = 'children',height = 300)

    ]),


], style = {'fontFamily':'helvetiva',
            'fontSize':18,
            'textAlign':'center'})



@app.callback(Output('wheels-output','children'),
              [Input('wheels','value')])
def callback_a(wheels_value):
    return "you chose {}".format(wheels_value)


@app.callback(Output('colors-output','children'),
              [Input('colors','value')])
def callback_b(color_value):
    return "you chose {}".format(color_value)


@app.callback(Output('display-image','src'),
              [Input('wheels','value'),
               Input('colors','value')])
def callback_image(wheel,color):
    return encode_image(df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])



if __name__ == '__main__':
    app.run_server(
        port=8050,
        host='0.0.0.0',
        debug=False)  
