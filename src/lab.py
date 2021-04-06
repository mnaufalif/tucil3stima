from queue import PriorityQueue
class A():
    def __init__(self, a):
        A.a = a

class B():
    def __init__(self):
        self.b = []
    
    def add(self, A):
        self.b.append(A)

a = A("newa")
b = B()

# pq = PriorityQueue()
# pq.put((1,"a"))
# pq.put((13,b))
# pq.put((5,"c"))
# print(pq.get())
# pq.put((3, b))
# print(pq.get())
# print(pq.get())
# print(pq.get())

l = [1,2,3]
l.insert(2,'e')
print(l)