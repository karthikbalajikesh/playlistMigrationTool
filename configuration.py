from distutils.command.config import config
from dotenv import load_dotenv
import toml
import os

class Configuration:
    def __init__(self) -> None:
        configs = toml.load("config.toml")
        # load the variables
        load_dotenv()

        self.spotifyClientId = os.getenv("SpotifyClientId")
        self.spotifyClientSecret = os.getenv("SpotifyClientSecret")
        self.spotifyUsername = os.getenv("SpotifyUserName")
        self.youtubeApiKey = os.getenv("YoutubeApiKey")
        self.hasFilter = configs['filter']
        self.playlistsToFilter = configs['playlistsToFilter']
        self.baseYoutubeSearch = configs['baseYoutubeSearch']
        self.googleClientId = os.getenv("GoogleClientId")
        self.googleClientSecret = os.getenv("GoogleClientSecret")
        self.googleClientSecretFile = os.getenv("GoogleClientSecretFile")
        self.baseYoutubeVideoLink = configs['baseYoutubeVideoLink']
        self.youtubeMaxSearchEntries = int(configs['youtubeMaxEntriesInSearch'])
        self.youtubeMinViewsThresholdMills = int(configs['youtubeMinViewsThresholdMills'])
        # TODO error handling for missing keys
        
        
# Test code
if __name__ == '__main__' :
    configs = Configuration()