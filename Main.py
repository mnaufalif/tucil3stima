from helper import distance
from node import Node
from graph import Graph
from algorithm import a_star

def test_distance():
    origin = str(input("Origin: ")).split(' ')
    destination = str(input("Destination: ")).split(' ')
    print("Jarak = %f km"%(distance(float(origin[0]), float(origin[1]), float(destination[0]), float(destination[1]))))

def test_node():
    # read from file
    filename = str(input("nama file: "))
    if(len(filename) <= 4 or filename[-4:] != '.txt'):
        filename+=".txt"
    path = "./test/"+filename

    with open(path, 'r') as f:
        nodes = f.read().split('\n')
        for i in range(len(nodes)):
            nodes[i] = nodes[i].split(' ')
        for node in nodes:
            Node(str(node[2]), float(node[0]), float(node[1]))
    # END read

    # show
    for node in Node.list_node:
        print(node.name)
    Node.reset()
    print(len(Node.list_node))
    # END show

def test_graph():
    Graph.read_node()
    Graph.read_adj()
    


def read_node():
    filename = str(input("nama file: "))
    if(len(filename) <= 4 or filename[-4:] != '.txt'):
        filename+=".txt"
    path = "./test/"+filename

    with open(path, 'r') as f:
        nodes = f.read().split('\n')
        for i in range(len(nodes)):
            nodes[i] = nodes[i].split(' ')
        for node in nodes:
            Node(str(node[2]), float(node[0]), float(node[1]))

if __name__ ==  "__main__":
    # read_node() # membaca node dari file
    test_graph()
    a_star()