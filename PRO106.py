import plotly.express as ps
import csv
import numpy as np

def graph(path):
  with open (path) as f:
    dataFrame=csv.DictReader(f)
    fig = ps.scatter(dataFrame,x="Marks In Percentage",y="Days Present")
    fig.show()
def getdatasource(path):
  ms = []
  dp = []
  with open(path) as g:
    df = csv.DictReader(g)
    for row in df:
      ms.append(float(row["Marks In Percentage"]))
      dp.append(float(row["Days Present"])) 
  return{"x":ms,"y":dp}
def correlate(datasource):
  cr = np.corrcoef(datasource["x"],datasource["y"])
  print(cr[0,1])
def setup():
  path = 'data3.csv'
  datasource = getdatasource(path)
  correlate(datasource)
  graph(path)

setup()