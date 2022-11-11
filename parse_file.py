from Player import Player

def read_argument(file):   
    """Reads name of data file""" 
    try:
        f = open(file, "r")
    except:
        raise ValueError("wrong name of file, try e.g. data.txt")
    return f

def initialize_points(f):
    players = {}
    dont_visit = []
    for line in f:
        data = line.split()
        id = int(data[0])
        x = float(data[1])
        y = float(data[2])

        if id in dont_visit:
            continue
        if len(data) > 3: # allows an arbitrary number of connections
            cons = [int(c) for c in data[3:]]
            players[id] = Player(id,x,y, cons)
        else: # if no connection, no need to visit this id
            dont_visit.append(id)
    V = id
    return players, V, dont_visit