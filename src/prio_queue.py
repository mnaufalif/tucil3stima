class PriorityQueue():
    def __init__(self):
        self.pq = []

    def put(self, item_tuple):
        try:
            push_last = True
            for i in range(len(self.pq)):
                if (self.pq[i][0] > item_tuple[0]):
                    self.pq.insert(i, item_tuple)
                    push_last = False
                    break
            if push_last:
                self.pq.append(item_tuple)
        except:
            print("input format not satisfied!")
    
    def get(self):
        return self.pq.pop(0)
    
    def del_by_key(self, key):
        for i in range(len(self.pq)):
            if self.pq[i][0] == key:
                self.pq.pop(i)
                break
    
    def check_value(self, value):
        for i in range(len(self.pq)):
            if id(self.pq[i][1]) == id(value):
                return True
        return False
