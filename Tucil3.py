import math as m
import folium as fl
from helper import distance
from node import Node
from graph import Graph
from algorithm import a_star

def read_data():
    Graph.read_node()
    Graph.read_adj()

read_data()
final_path = a_star()



# Drawing Base
Map = fl.Map(location=[-6.935373, 107.633486], width=800, height=512, zoom_start=15)

for i in range(0, len(Graph.nameList)):
    fl.Marker(
        location=[Graph.latList[i], Graph.lngList[i]],
        popup=Graph.nameList[i],
        icon=fl.Icon(color="blue"),
    ).add_to(Map)
    

point1=[]
point2=[]
for i in range (0, len(Graph.adjmatrix)):
    for j in range (0, len(Graph.adjmatrix[i])):
        if(Graph.adjmatrix[i][j]!='0'):
            point1= [Graph.latList[i], Graph.lngList[i]]
            point2= [Graph.latList[j], Graph.lngList[j]]
            Graph.edgesList+=[[point1, point2]]
        point1=[]
        point2=[]

    
for i in Graph.edgesList:
    fl.PolyLine(i, color='blue').add_to(Map)

#- adding final_path to map
EdgesList = []
for i in range(len(final_path)-1):
    point1 = [final_path[i].lat, final_path[i].lng]
    point2 = [final_path[i+1].lat, final_path[i+1].lng]
    EdgesList+=[[point1, point2]]
    point1=[]
    point2=[]

for i in EdgesList:
    fl.PolyLine(i, color='orange').add_to(Map)



Map