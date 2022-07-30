from dotenv import load_dotenv
import toml
import os

class Configuration:
    def __init__(self) -> None:
        configs = toml.load("config.toml")
        # load the variables
        load_dotenv()

        self.clientId = os.getenv("clientId")
        self.clientSecret = os.getenv("clientSecret")
        self.username = os.getenv("userName")
        self.hasFilter = configs['filter']
        self.playlistsToFilter = configs['playlistsToFilter']

        print(self.playlistsToFilter)

# Test code
if __name__ == '__main__' :
    configs = Configuration()