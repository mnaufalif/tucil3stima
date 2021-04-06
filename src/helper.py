import math as m

def distance (Lat1, Lng1, Lat2, Lng2):
    r = 6371 #radius bumi
    Lat1=m.radians((Lat1))    
    Lat2=m.radians((Lat2))    
    Lng1=m.radians((Lng1))    
    Lng2=m.radians((Lng2))    
    dlat = (Lat1-Lat2)
    dlng = (Lng1-Lng2)
    return 2*r*(m.asin((m.sqrt(m.sin(dlng/2)**2 + m.cos(Lat1)*m.cos(Lat2)*m.sin(dlat/2)**2))))  

