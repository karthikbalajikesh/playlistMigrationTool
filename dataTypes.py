
from unicodedata import name


class Song:
    def __init__(self,name:str, artist:str) -> None:
        self.name = name
        self.artist = artist
        
    def getSearchString(self)->str:
        return "{name} song by {artist}".format(name=self.name, artist=self.artist)



