# smurftown
Main file

# computations
All utility functions for finding cycles and computing distances.

# parse_file
Functions for used for parsing and initializing point/player objects

# Player
Player class that will hold data for id,x,y, and a list of connections

# generate_data
Program that could be used to generate data.txt files: 

## Example usage
`python generate_data.py -b10 -n1000 -c2 data.txt`

Genererates a file called *data.txt* which contains 1000 points (n=1000), each with a maximum of 2 connections (c=2) and with a boundary of 10 (e.g. x=[-10,10])

# Instructions for running program
Start by generating a data file (*data.txt*) if it does not exist.
## 1) Generate data file
Either by:
`python generate_data.py -b10 -n1000 -c2 data.txt`

or by:
`make gen_data`

where the latter is generated though a makefile.
## 2) Run program
Run the program, either through:
`python smurftown.py name_of_the_data_file.txt`

or by:
`make`

where the latter runs the program with the file that was generated though *make gen_data*


