import dash
import dash_core_components as dcc
import dash_html_components as html
from scrapedData import Open


Y1 , X1 = Open()

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Board'),
    dcc.Graph(id = 'example',
              figure={
                  'data':[
                      {'x':X1,'y':Y1,'type':'line','name':'boats'},

                  ],
                  'layout':{
                        'title':'Basic Dash'
}
                  })

])

if __name__ =='__main__':
    app.run_server(debug=True)