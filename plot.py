import pandas
import plotly.graph_objects as go

data = pandas.read_csv("data.csv")

figure = go.Figure()
figure.add_trace(go.Scatter(x=data['t'], y=data['x'], name='X'))
figure.add_trace(go.Scatter(x=data['t'], y=data['y'], name='Y'))
figure.add_trace(go.Scatter(x=data['t'], y=data['z'], name='Z'))
figure.add_trace(go.Scatter(x=data['t'], y=data['w'], name='W'))
figure.show()

