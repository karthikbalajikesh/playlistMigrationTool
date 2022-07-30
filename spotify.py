import tekore as sp
from dataTypes import Song
from configuration import Configuration

class SpotifyClient:
    def __init__(self, config:Configuration) -> None:
        self.clientId = config.clientId
        self.clientSecret = config.clientSecret
        self.username = config.username
        self.config = config
        self.token = sp.request_client_token(self.clientId, self.clientSecret)
        self.spotify = sp.Spotify(self.token)

        print("Spotify client construction complete")


    def getPlaylistNames(self) ->list :
        playlists = self.spotify.playlists(user_id=self.username)
        result = []
        for playlist in playlists.items:
            result.append(playlist.name)
        
        return result

    def getPlaylistNamesWithIds(self) ->dict :
        playlists = self.spotify.playlists(user_id=self.username)
        result = {}
        for playlist in playlists.items:
            result[playlist.name] = playlist.id
        
        return result

    def getSongsForPlaylist(self, playlistName:str) -> 'list[Song]':
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



