#!/usr/bin/env python

import argparse

'''samparse_2.py improves on samparse.py by adding args and taking a sam file with header.'''

def get_args():
    parser = argparse.ArgumentParser(description="Takes a SAM file and calculates count of genes mapped or unmapped.")
    parser.add_argument("-f", "--readfile", help="SAM file to read", required=True, type=str)
    parser.add_argument("-w", "--writefile", help="Text file name to write to", required=True, type=str)
    return parser.parse_args()
args = get_args()

#initialize empty list and variables
reads: list=[]
mapped = 0
notmapped = 0

with open(args.readfile, "r") as fh, open(args.writefile, "w") as wh: #create read and write filehandles
    for line in fh: #iterate over file, and for every line:
        if not (line.startswith("@")):
            line = line.strip() #strip newline character
            line = line.split("\t") #split the line at tab characters
            flag = int(line[1]) #assign flag to the value of column 2 (convert from string to int)
            if ((flag & 256)) != 256: #if bitwise flag for 256 is not selected (NOT secondary alignment)
                if((flag & 4) != 4): #then if the bitwise flag for 4 is not selected (NOT unmapped)
                    mapped += 1
                else: #if the bitwise flag for 4 IS selected (unmapped)
                    notmapped += 1
    wh.write(f"Mapped: {mapped}\nNotmapped: {notmapped}") #write to file.