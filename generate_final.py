import os

outfile=open("final.cust", "w")
outtext = ""

break_time = 20

for i in os.listdir("CUST"):
    print i
    outtext += open("CUST/" + i).read()
    outtext += " " * break_time

outfile.write(outtext)