import argparse
import random 

parser = argparse.ArgumentParser()
parser.add_argument(
  '-b', type=int, default=10, help='coordinate bound')
parser.add_argument(
  '-n', type=int, help='number of points')
parser.add_argument(
  '-c', type=int, help='max number of connections')
parser.add_argument(
  'output_name', metavar='output', type=str,
  help='output file name')
args = parser.parse_args()


def create_data(b, c, n, i):
    x = round(random.uniform(-b, b),1)
    y = round(random.uniform(-b, b),1)

    # number of connections
    num_c = random.randint(0,c) 

    con = random.sample(range(1,n+1), num_c)
    while i in con:
        con = random.sample(range(1,n+1), num_c)

    string_con = ""
    for st in con:
        string_con += str(st) + " "
    return str(i) + " " + str(x) + " " + str(y) + " " + string_con + "\n"

with open(args.output_name, 'w') as output:
    output.writelines((create_data(args.b,args.c, args.n, i))
                        for i in range(1,args.n+1) )

# Usage
# >>> python generate_data.py -b2 -n5 -c2 data_test.txt