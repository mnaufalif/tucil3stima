from helper import distance
from node import Node
FILE_PATH = "./test/"

class Graph:
    nodesList=[]
    edgesList=[]
    adjmatrix=[]
    latList=[]
    lngList=[]
    nameList=[]

    def __init__(self):
        pass

    def AddNode(self, Lat, Lng):
        if[Lat, Lng] not in Graph.nodesList:
            Graph.nodesList+=[[Lat, Lng]]
            Graph.latList+=[Lat]
            Graph.lngList+=[Lng]
    
    def read_node():
        KoorFile = input("Masukkan nama file koordinat (tulis tanpa .txt) : ")
        filename = FILE_PATH+KoorFile+".txt"
        f = open(filename, "r")
        file_contents = f.read().splitlines()
        f.close()

        temp=[]
        for i in file_contents:
            temp+=i.split()
            
        for i in range (0, len(temp)):
            if i%3==0:
                Graph.latList+=[float(temp[i])]
            elif i%3==1:
                Graph.lngList+=[float(temp[i])]
            elif i%3==2:
                Graph.nameList+=[temp[i]]

        path = filename
        with open(path, 'r') as f:
            nodes = f.read().split('\n')
            for i in range(len(nodes)):
                nodes[i] = nodes[i].split(' ')
            for node in nodes:
                Node(str(node[2]), float(node[0]), float(node[1]))



    def read_adj():
        AdjFile = input("Masukkan file adjacency matrix (tulis tanpa .txt) : ")
        filename2=FILE_PATH+AdjFile+".txt"
        f = open(filename2, "r")
        file_contents2 = f.read().splitlines()
        f.close()
            
        for i in file_contents2:
            i=i.split()
        for i in range (0, len(file_contents2)):
            Graph.adjmatrix+=[file_contents2[i].split()]


        for i in range (0, len(Graph.adjmatrix)):
            for j in range (0, len(Graph.adjmatrix[i])):
                if(Graph.adjmatrix[i][j]=='1'):
                    Graph.adjmatrix[i][j]=distance(Graph.latList[i], Graph.lngList[i], Graph.latList[j], Graph.lngList[j])

