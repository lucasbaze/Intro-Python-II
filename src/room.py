# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.positions = ['nope', 'nope', 'nope', 'nope']
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name} :: {self.desc}"

    def options(self):
        print(f"North: {self.n_to}")
        print(f"East: {self.e_to}")
        print(f"South: {self.s_to}")
        print(f"West: {self.w_to}")
