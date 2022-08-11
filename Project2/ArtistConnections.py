import random
import csv
from Vertex import *


class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """

    def load_graph(self, songLibaray):

        with open(songLibaray, 'r') as file:
            lines = file.readlines()
            for line in lines:
                items = line.split(',')
                artist = items[2]
                coArtists = items[5]
                if artist in self.vertList.keys():


                    self.vertList[artist].append(coArtists)


                else:
                    Vertex(artist)
                    self.vertList[artist] = coArtists[:len(coArtists) - 1].split(';')
                    self.numVertices = self.numVertices + 1


        print(self.vertList, self.numVertices)
        return self.numVertices

    """
    Return song libary information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)
    """

    def search_artist(self, artist_name):
        numSongs = 0
        print("Search By Artist ", artist_name, " ")

        if artist_name in self.vertList:
            numSongs += 1
            print(numSongs, " ", self.vertList.get(artist_name))
            return numSongs, self.vertList.get(artist_name)

        else:
            print("Artist not found")





    """       
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):
        two_hop_friends = []


        return two_hop_friends

    """
    Search the information of an artist based on the artist name
    """

    def recommend_new_collaborator(self, artist_name):
        artist = ""
        numSongs = 0

        #
        # Write your code here
        #

        return artist, numSongs

    """
    Search the information of an artist based on the artist name
    """

    def shortest_path(self, artist_name):
        path = {}

        #
        # Write your code here
        #
        return path


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    artistGraph = ArtistConnections()
    artistGraph.load_graph("TenKSongs.csv")
    artistGraph.search_artist("Mariah Carey")


