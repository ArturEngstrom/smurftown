import math
import multiprocessing as mp
def find_cycle(player, visited, dont_visit, f, players):
    if len(visited) != 0 and player.id == visited[0]: # if we found cycle
        return True, visited

    if player.id not in visited:
        visited.append(player.id)
    else: # not interested if id already in cycle
        return False, visited

    for c in player.connection:
        if c in dont_visit:
            continue

        is_cycle, visited = find_cycle(players[c], visited, dont_visit, f, players)
        if is_cycle:
            f.write(" ".join(str(v) for v in visited) +"\n")
            # print(visited)
            
    # if we reach this we have not found cycle
    visited.pop() # we can cosider this a Stack
    return False, visited

def compute_small_distance(p1,p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def compute_total_distance(visited_nodes, players):
    """Computes the total distance of a given path"""
    dist = 0
    for i,j in zip(visited_nodes, visited_nodes[1:]+[visited_nodes[0]]): #adding last element to compute the whole circle 
        dist += compute_small_distance(players[i], players[j])

    return round(dist,3)

def find_all_cycles(filename, players, dont_visit):
    """
    Depth first search DFS algorithm for finding cycles

    The cycles are written to a file where the user can crosscheck the validity
    """
    f = open(filename, "w", encoding='utf-8')
    for p in players:
        visited = []
        _, _ = find_cycle(players[p], visited, dont_visit, f, players)
    f.close()

def compute_distances_in_cycles(filename, players):
    """computes all distances in all found cycles"""
    f = open(filename, "r", encoding='utf-8')
    distances = {}
    for line in f:
        visited_nodes = [int(i) for i in line.split()]
        d = compute_total_distance(visited_nodes, players)
        if d not in distances:
            distances[d] = [visited_nodes]
        else:
            distances[d].append(visited_nodes)
    f.close()
    return distances

def compute_longest_path(filename,distances):
    f = open(filename, "w", encoding='utf-8')
    answered = False
    for d in reversed(sorted(distances)):
        if not answered:
            print(" ".join(str(v) for v in distances[d][0])) 
            answered = True
        f.write("dist: "+ str(d) + " \t path: " + " ".join(str(v) for v in distances[d][0]) +"\n")
    if not answered:
        print("No circular path found")
        f.write("No circular path found")
    f.close()
