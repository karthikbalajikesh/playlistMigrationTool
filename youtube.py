from unittest import result
import googleapiclient.discovery
import googleapiclient.errors
from requests import request
from configuration import Configuration
from dataTypes import Song


class YoutubeSearch:
    def __init__(self, configs:Configuration) -> None:
        self.apiKey = configs.youtubeApiKey
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.secretFile = configs.googleClientSecretFile
        self.youtubeClient = googleapiclient.discovery.build(self.api_service_name, self.api_version,developerKey = self.apiKey)
        self.maxSearchEntries = configs.youtubeMaxSearchEntries
        self.minViewsInMillions = configs.youtubeMinViewsThresholdMills
        self.baseYoutubeVideoLink = configs.baseYoutubeVideoLink

    def searchMostViewedSong(self,song:Song=None, songStr:str = None)->dict:
        return self.searchSong("viewCount",song,songStr)

    def searchMostRelevantSong(self, song:Song=None, songStr:str = None) ->dict:
        return self.searchSong("relevance",song,songStr)


    def searchSong(self,orderType:str,song:Song=None, songStr:str = None ):
        if(song == None) and (songStr == None):
            print("ERROR: Need either a song object or string")
        searchString = ""
        if (song==None):
            searchString = songStr
        else:
            searchString = song.getSearchString()
        request = self.youtubeClient.search().list(part="snippet", q = searchString, order=orderType, maxResults=self.maxSearchEntries)
        response = request.execute()
        return response

    def getViewCountForSongid(self, songId:str)->int:
        request = self.youtubeClient.videos().list(part="statistics", id=songId)
        response = request.execute()

        return int(response['items'][0]['statistics']['viewCount'])

    def getVideoIdForSong(self, song:Song):
        resultNum = 0
        gotResult = False
        searchResponse = self.searchMostRelevantSong(song=song)

        while(not gotResult):
            videoId = searchResponse['items'][resultNum]['id']['videoId']
            viewCountInMill = self.getViewCountForSongid(videoId)//1000000
            gotResult = True
            
            if(viewCountInMill < self.minViewsInMillions):
                print("The video {videoLink} has less than {min} million views.".format(videoLink=self.baseYoutubeVideoLink + videoId, min= self.minViewsInMillions))
                entry = int(input("Press 1 to add to the playlist anyways. Else press 0"))    
                if (entry == 1) :
                    gotResult = True # just for readability
                    return videoId
                else :
                    resultNum += 1
            # else send the result
            else :
                gotResult = True # just for readability
                return videoId

            if resultNum >= self.maxSearchEntries:
                print("ERROR: No good video found")
                return None

        
        

        



if __name__ == '__main__':
    configs = Configuration()
    youtube = YoutubeSearch(configs)

    song = Song("Numb","Linkin Park")
    print(youtube.getVideoIdForSong(song))



    

