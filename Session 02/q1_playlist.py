Playlist = [
    "Shape of You",
    "Blinding Lights",
    "Believer",
    "Perfect"
    ]


class playlistManager():
    def __init__(self, list):
        self.list = list

    # A. Count elements in List
    def trackCounter(self):
        print(f"You have {len(self.list)} Music in your Playlist.")

    # B. Return the First and the Last Music
    def lastFirstMusic(self):
        print(f"The First track is : {self.list[0]}")
        print(f"The Lasr track is : {self.list[-1]}")

    # Add "Dynamite"
    def appendDynamite(self):
        self.list.append("Dynamite")
        print(f"\"Dynamite\" Addeed to playList successfully :) \n New PlayList is: {self.list} ")

    # Ommit "Believer"
    def removeBeliever(self):
        isExist = "Believer" in self.list
        self.list.remove("Believer") if isExist else print("'Believer' is already removed")
        print(self.list)

    # Sort list in order (A-Z)
    def playlistSorter(self):
        self.list.sort()
        print(f"Sorted List:\n {self.list} ")

    # Print playlisy with Index
    def PrintPlaylist(self):
        print("Playlist Items: ")
        for Music in self.list:
            print(f"\t{self.list.index(Music) + 1}. {Music}")


Manager = playlistManager(Playlist)
Manager.trackCounter()
Manager.lastFirstMusic()
Manager.appendDynamite()
Manager.removeBeliever()
Manager.playlistSorter()
Manager.PrintPlaylist()
