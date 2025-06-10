class Coordenadas:
    def __init__(self, latitude, longuitude):
        self.lat = latitude
        self.lon = longuitude
    def __eq__(self, value):
        return self.lat == value.lat and self.lon == value.lon
    
    def __ne__(self, value):
        return self.lat != value.lat or self.lon != value.lon
    
    def __lt__(self, value):
        return self.lat + self.lon < value.lat + value.lon
    
    def __le__(self, value):
        return self.lat + self.lon <=  value.lat + value.lon
  
    
coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)
print(coords > coords2)
print(coords <= coords2)