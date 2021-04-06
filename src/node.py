from helper import distance
class Node():
    INFINITY_R = -1
    list_node = []
    node_count = 0

    start_node_id = None
    end_node_id = None

    list_distance = [] # list jarak tiap node ke end_node

    def __init__(self, name, lat, lng):
        Node.node_count += 1
        self.id = int(Node.node_count) 
        self.name = name
        self.lat = lat
        self.lng = lng

        self.prev_distance = Node.INFINITY_R
        self.prev_node = None

        Node.list_node.append(self)

    def __del__(self):
        # print("node %d destroyed"%(self.id))
        pass

    def set_start(id):
        valid = False
        for node in Node.list_node:
            if node.id == id:
                valid = True
                break
        if valid:
            Node.start_node_id = int (id)
        else:
            print("Invalid Node!")

    def set_end(id):
        # jika valid, melakukan set end_node dan menghitung jarak tiap-tiap node ke end_node
        valid = False
        for node in Node.list_node:
            if node.id == id:
                valid = True
                break
        if valid:
            Node.end_node_id = int (id)
            Node.calculate_distances()
        else:
            print("Invalid Node!")

    def update_prev_distance(self, prev_distance):
        self.prev_distance = float(prev_distance)

    def update_prev_node(self, prev_node_reference):
        self.prev_node = prev_node_reference

    def get_start_node():
        if (Node.start_node_id == None):
            return None
        ret = None
        for node in Node.list_node:
            if node.id == Node.start_node_id:
                ret = node
                break
        return ret

    def get_end_node():
        if (Node.end_node_id == None):
            return None
        ret = None
        for node in Node.list_node:
            if node.id == Node.end_node_id:
                ret = node
                break
        return ret

    def get_index(self):
        return int(self.id-1)

    def get_node(id):
        i = 0
        while i<len(Node.list_node):
            if(Node.list_node[i].id == id):
                return Node.list_node[i]
            i+=1
        return None

    def set_start_end_handler():
        print("--=Set start-end=--")
        Node.print_all()
        Node.set_start(int(input("start: ")))
        Node.set_end(int(input("end: ")))


    def calculate_distances():
        end_node = Node.get_end_node()
        for node in Node.list_node:
            d = distance(node.lat, node.lng, end_node.lat, end_node.lng)
            Node.list_distance.append(d)

    def print_all():
        i = 0
        for node in Node.list_node:
            i += 1
            print("[%d] %s"%(i,node.name))

    def reset():
        i=0
        while i < len(Node.list_node):
            del Node.list_node[i]
        Node.list_node = []
        Node.node_count = 0
        Node.start_node_id = None
        Node.end_node_id = None
        print("reset success")
