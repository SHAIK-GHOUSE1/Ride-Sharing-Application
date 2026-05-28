from math import sqrt
class Location:
    def __init__(self,latitude:float,longitude:float):
        self.__latitude:float=latitude
        self.__longitude:float=longitude
    def get_latitute(self)->float:
        return self.__latitude
    
    def get_longitude(self)->float:
        return self.__longitude
    def __calcDistance(self,loc:Location):
        # Euclidean Distanc
        dx:float=self.get_latitute()-loc.get_latitute()
        dy:float=self.get_longitude()-loc.get_longitude()
        return sqrt(dx*dx + dy*dy)