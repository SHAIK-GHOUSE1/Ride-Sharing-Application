class Location:
    def __init__(self,latitude:float,longitude:float):
        self.__latitude:float=latitude
        self.__longitude:float=longitude
    def get_latitute(self)->float:
        return self.__latitude
    
    def get_longitude(self)->float:
        return self.__longitude
  