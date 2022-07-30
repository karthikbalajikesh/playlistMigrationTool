import tekore as sp
from dataTypes import Song
from configuration import Configuration

class SpotifyClient:
    def __init__(self, config:Configuration) -> None:
        self.clientId = config.spotifyClientId
        self.clientSecret = config.spotifyClientSecret
        self.username = config.spotifyUsername
        self.config = config
        self.token = sp.request_client_token(self.clientId, self.clientSecret)
        self.spotify = sp.Spotify(self.token)

        print("Spotify client construction complete")


    def getPlaylistNames(self) ->list :
        '''
        Function gets the list of playlists for the username provided in the configs
        '''
        playlists = self.spotify.playlists(user_id=self.username)
        result = []
        for playlist in playlists.items:
            result.append(playlist.name)
        
        return result

    def getPlaylistNamesWithIds(self) ->dict :
        '''
        Function gives the map between every playlist with their hash ids
        '''
        playlists = self.spotify.playlists(user_id=self.username)
        result = {}
        for playlist in playlists.items:
            result[playlist.name] = playlist.id
        
        return result

    def getSongsForPlaylist(self, playlistName:str) -> 'list[Song]':
        '''
        Gets a list of songs for a playlist queried
        '''
        result = []
        playlistsWithIds = self.getPlaylistNamesWithIds()
        if not playlistName in playlistsWithIds:
            return result
        
        playlistId = playlistsWithIds[playlistName]

        playlistInfo = self.spotify.playlist(playlistId)
        for track in playlistInfo.tracks.items:
            result.append(Song(track.track.name, track.track.artists[0].name)) # only supporting one artist

        return result


if __name__ == '__main__':
    configs = Configuration()
    spotify = SpotifyClient(configs)

    # print(spotify.getPlaylistNamesWithIds())
    songList = spotify.getSongsForPlaylist("Vibe")
    for song in songList:
        print(song.getSearchString())



