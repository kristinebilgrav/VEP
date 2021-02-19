mport sys
import os

#filtering vep output file based on flag (>5)

fileInput = open(sys.argv[1], "r") # txt file with vep output paths

for line in fileInput:
    line = line.strip("\n")
    name = (line.split("/")[-1].split("."))
    filename = name[-4] + "_f.vcf"
    file = open(line, "r")
    fileOutput = open(filename, "w")
    for l in file:
        l = l.strip("\n")
        if l.startswith("#"):
            fileOutput.write(l + "\n")
            continue
        flags  = l.split("CLIP3 ")[-1].split("\t")[-1].split(":")
        theflag = flags[2] #string
        if int(theflag) > 5:
            fileOutput.write(l + "\n")
           


