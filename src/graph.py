from helper import distance
from node import Node
FILE_PATH = "../test/"

class Graph:
    nodesList=[]
    edgesList=[]
    adjmatrix=[]
    latList=[]
    lngList=[]
    nameList=[]
    location=""
    filename = ""
    starting_view_coordinate = []

    def __init__(self):
        pass

    def AddNode(self, Lat, Lng):
        if[Lat, Lng] not in Graph.nodesList:
            Graph.nodesList+=[[Lat, Lng]]
            Graph.latList+=[Lat]
            Graph.lngList+=[Lng]
    
    def read_data():
        # MENU
        supported_area = []
        input_valid = False
        selected_area = ""
        
        with open(FILE_PATH+"supported_area.txt", "r") as f:
            supported_area = f.read().split('\n')
        while not input_valid:
            print("Pilih Daerah:")
            for i in range(len(supported_area)):
                print("[%d] %s"%(i+1, supported_area[i]))
            x = int(input(" >> "))
            if 0 < x and x <= len(supported_area):
                input_valid = True
            else:
                print("Masukan tidak valid.") 
        selected_area = str(supported_area[x-1])


        # Baca Koor
        Graph.location = "Koor"+selected_area
        Graph.filename = FILE_PATH+selected_area+'/'+Graph.location+".txt"
        f = open(Graph.filename, "r")
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

        path = Graph.filename
        with open(path, 'r') as f:
            nodes = f.read().split('\n')
            for i in range(len(nodes)):
                nodes[i] = nodes[i].split(' ')
            for node in nodes:
                Node(str(node[2]), float(node[0]), float(node[1]))


        # Baca Adj
        AdjFile = "Adj"+selected_area
        filename2=FILE_PATH+selected_area+'/'+AdjFile+".txt"
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


        # Baca starting_view_coordinate
        ViewFile = "View"+selected_area
        with open(FILE_PATH+selected_area+'/'+ViewFile+".txt", "r") as f:
            start_koor = f.read().split(' ')
            Graph.starting_view_coordinate = start_koor