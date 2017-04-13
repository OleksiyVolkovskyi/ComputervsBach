import os

for i in os.listdir("retCSV"):
    print i
    os.system(". midicsv-1.1/csvmidi ./retCSV/" + i + " ./retMidi/" + i[:-3] + "mid")