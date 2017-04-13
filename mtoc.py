import os

for i in os.listdir("MIDI"):
    print i
    os.system("midicsv-1.1\\Midicsv.exe ./MIDI/" + i + " ./CSV/" + i[:-3] + "csv")