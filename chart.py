import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Board'),
    dcc.Graph(id = 'example',
              figure={
                  'data':[
                      {'x':[1,2,3,4,5],'y':[1,5,6,7,3],'type':'line','name':'boats'},
                      {'x':[1,2,3,4,5],'y':[2,9,3,4,6],'type':'bar','name':'cars'}
                  ],
                  'layout':{
                        'title':'Basic Dash'
}
                  })

])

if __name__ =='__main__':
    app.run_server(debug=True)