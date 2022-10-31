import plotly.express as px
from random import randint


data: list = [randint(0, 6) for _ in range(23)]
fig = px.bar(y=data)

fig.show()

