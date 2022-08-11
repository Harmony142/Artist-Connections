from SongLibrary import SongLibrary
from ArtistConnections import *
import re

class DFA:

    def __init__(self, s=None):
        self.start = s

    """
    Build the DFA graph from the figure in task 2
    """

    def build_DFA(self):

        self.start = Vertex(0)  # Initializes states vertices
        self.v1 = Vertex(1)
        self.v2 = Vertex(3)
        self.v3 = Vertex(3)
        self.v4 = Vertex(4)
        self.v5 = Vertex(5)
        self.v6 = Vertex(6)
        self.v7 = Vertex(7)

        self.v7.setAcceptingState() # Sets v7 as the final state

        self.start.addEdge(Edge("A", self.v1))  # Adds conditions between states as edges
        self.v1.addEdge(Edge("C", self.v2))
        self.v1.addEdge(Edge("A", self.v1))
        self.v2.addEdge(Edge("A", self.v3))
        self.v3.addEdge(Edge("T", self.v1))
        self.v3.addEdge(Edge("C", self.v4))
        self.v4.addEdge(Edge("A", self.v5))
        self.v5.addEdge(Edge("C", self.v4))
        self.v5.addEdge(Edge("T", self.v1))
        self.v5.addEdge(Edge("G", self.v6))
        self.v6.addEdge(Edge("A", self.v7))
        self.v7.addEdge(Edge("C", self.v2))
        self.v7.addEdge(Edge("A", self.v1))

    """
    Test whether the input sequence seq will be accepted by the state machine
    return True if accept
    """
    def testMatch(self, seq):
        self.characters = list(seq)  # Separates the DNA sequence into an iterable list of characters
        self.current = self.start    # Sets the current vertex to start

        for char in self.characters: # for each character in the list
            if self.current == None:
               # print("No Match")
                return False
            self.current = self.current.followEdge(char)  # Follows path from vertex one to the destination vertex connected via char
            if self.current == self.v7:
                #print("Match")
                return True

        return False

    """
    Test whether the one suffix of the input sequence seq will be accepted by the state machine
    return the index position if accept
    return -1 if not accept
    """
    def testAccept(self, seq):
        indx = -1

        for i in range (len(seq) - 1): # iterate through the range of the given DNA sequence

            if self.testMatch(seq[i:]): # determines whether or not the sub string will be accepted by the state machine
                    return i # returns the initial position where the substring is accepted

        return indx

    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file
    """
    def testSongLibrary(self, song_lib):

        matchIndx = []
        songs = song_lib.songArray

        for song in songs: # for every song in the song list
            if self.testAccept(song.DNA) != -1: # if the FSA accepts the DNA sequence or any substring of it
                matchIndx.append(self.testAccept(song.DNA)) # append the index of the accepted substring to matchIndx

            else:  # if the FSA does not accept the sequence
                matchIndx.append(-1) # append -1 to machIndx
        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    dfa = DFA()
    dfa.build_DFA()
    song_lib = SongLibrary()
    song_lib.loadLibrary()
    dfa.testSongLibrary(song_lib)
    dfa.testMatch("AACATACACATACACAGACACAGA")
    dfa.testAccept("TTACACAGA")

    print("finish")