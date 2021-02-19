import sys
import os

#runs through files in txt file  and creates file for each MEs for each individual

fileInput = open(sys.argv[1], "r") # txt file with vep output paths

for line in fileInput:
    line = line.strip("\n")
    name = (line.split("/")[-1].split("."))
    filename = name[-4]
    file = open(line, "r")
    fileOutputA = open(filename + "_Alu.vcf", "w")
    fileOutputL = open(filename + "_L1.vcf", "w")
    fileOutputSVA = open(filename + "_SVA.vcf", "w")
    fileOutputHERV = open(filename + "_HERV.vcf", "w")

    for l in file:
        l = l.strip("\n")
        if l.startswith("#"):
            fileOutputA.write(l + "\n")
            fileOutputL.write(l + "\n")
            fileOutputSVA.write(l + "\n")
            fileOutputHERV.write(l + "\n")
            continue
        if "ALU" in l:
            fileOutputA.write(l + "\n")
        if "L1" in l:
            fileOutputL.write(l + "\n")
        if "SVA" in l :
            fileOutputSVA.write(l + "\n")
        if "HERV" in l:
            fileOutputHERV.write(l + "\n")

