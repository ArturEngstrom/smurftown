import sys
from computations import find_all_cycles, compute_distances_in_cycles, compute_longest_path
from parse_file import read_argument, initialize_points
import time

if __name__ == "__main__":
    benchmark = True
                                                                    # n=100, c=2    n=1k, c=2       n=10k, c=2      n=20k, c=2
    t1 = time.time()
    file = read_argument(file=sys.argv[1])                          # Time=0.00023  Time=0.00006    Time=0.00005    Time=0.00006 
    t2 = time.time()
    if benchmark: 
        print("1) Time=%.5f" % (t2 - t1))
    players, V, dont_visit = initialize_points(file)                # Time=0.00069  Time=0.00591    Time=0.21943    Time=0.84539
    t3 = time.time()
    if benchmark: 
        print("2) Time=%.5f" % (t3 - t2))
    filename = "all_cycles_including_doublets.txt"      
    find_all_cycles(filename, players, dont_visit)                  # Time=0.00098  Time=0.08576    Time=12.47905   Time=82.84812
    t4 = time.time()
    if benchmark: 
        print("3) Time=%.5f" % (t4 - t3))
    distances = compute_distances_in_cycles(filename, players)      # Time=0.00022  Time=0.00028    Time=0.00223    Time=0.00387
    t5 = time.time()
    if benchmark: 
        print("4) Time=%.5f" % (t5 - t4))
    filename2 = "all_cycles_final.txt"
    compute_longest_path(filename2,distances)                       # Time=0.00040  Time=0.00027    Time=0.00031    Time=0.00043
    t6 = time.time()
    if benchmark: 
        print("5) Time=%.5f" % (t6 - t5))

