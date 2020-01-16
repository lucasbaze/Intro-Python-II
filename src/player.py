# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, location='outside'):
        self.location = location

    def move(self, location):
        self.location = location

    def where(self):
        print(self.location)
