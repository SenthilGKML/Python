import glob2
import time

filenames=glob2.glob("*.txt")

with open("new.txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")