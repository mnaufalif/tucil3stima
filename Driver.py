def sqrt(n):
  ans = n ** 0.5
  return ans

def factorial(n):
  k = 1
  for i in range(1, n+1):
    k = i * k

  return k 

def sin(d):
  pi = 3.14159265359
  n = 180 / int(d) # 180 degrees = pi radians
  x = pi / n # Converting degrees to radians
  ans = x - ( x ** 3 / factorial(3) ) + ( x ** 5 / factorial(5) ) 
  return ans 

def cos(d):
  pi = 3.14159265359
  n = 180 / int(d) 
  x = pi / n 
  ans = 1 - ( x ** 2 / factorial(2) ) + ( x ** 4 / factorial(4) ) 
  return ans 

# def arcsin(x):


# def distance (Lat1, Lng1, Lat2, Lng2):
#     return 

#//////////////////////////////////////////////
KoorFile = input("Masukkan nama file koordinat (tulis tanpa .txt) : ")
filename = "./src/"+KoorFile+".txt"
f = open(filename, "r")
file_contents = f.read().splitlines()
f.close()

temp=[]
for i in file_contents:
    temp+=i.split()

lat=[]
lng=[]
name=[]
for i in range (0, len(temp)):
    if i%3==0:
        lat+=[temp[i]]
    elif i%3==1:
        lng+=[temp[i]]
    elif i%3==2:
        name+=[temp[i]]

print(lat)
print(lng)
print(name)

AdjFile = input("Masukkan file adjacency matrix (tulis tanpa .txt) : ")
filename2="./src/"+AdjFile+".txt"
f = open(filename2, "r")
file_contents2 = f.read().splitlines()
f.close()

for i in file_contents2:
    i=i.split()

AdjMatrix = []
for i in range (0, len(file_contents2)):
    AdjMatrix+=[file_contents2[i].split()]
print(AdjMatrix)

# print(sin(90))
# print(arcsin(1))