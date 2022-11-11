class Player:
    def __init__(self, id, x, y, c = None):
        self.id = id
        self.x = x
        self.y = y
        # connections
        self.connection = c
    def verbose(self):
        print("ID:",self.id,
              "(x,y)", self.x, self.y,
              "con", self.connection)

