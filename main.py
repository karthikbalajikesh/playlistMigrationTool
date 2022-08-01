# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python


from configuration import Configuration
from spotify import SpotifyClient
from youtube import YoutubeSearch


def main():
    configs = Configuration()
    youtubeSearch = YoutubeSearch(configs)
    spotify = SpotifyClient(configs)
    songList = spotify.getSongsForPlaylist("Vibe")

    for song in songList:
        print(youtubeSearch.getVideoIdForSong(song))

    

if __name__ == "__main__":
    main()