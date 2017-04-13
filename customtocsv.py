import os

def run(inpath, outpath):
    infile = open(inpath).read()
    outfile = open(outpath, "w")
    outtext = """0, 0, Header, 1, 2, 480
1, 0, Start_track
1, 0, Title_t, "Close Encounters"
1, 0, Text_t, "Sample for MIDIcsv Distribution"
1, 0, Copyright_t, "This file is in the public domain"
1, 0, Time_signature, 4, 2, 24, 8
1, 0, Tempo, 500000
1, 0, End_track
2, 0, Start_track
2, 0, Instrument_name_t, "Solo Lute or Keyboard"
2, 0, Program_c, 0, 19
"""

    step_size = 1
    time_point = 0

    notes_on = []
    
    """for i in infile:
        if i == " ":
            time_point += step_size
        else:
            if not i in notes_on:
                outtext += "2, " + str(time_point) + ", Note_on_c, 0, " + str(ord(i)) + ", 100\n"
                notes_on.append(i)
            else:
                outtext += "2, " + str(time_point) + ", Note_off_c, 0, " + str(ord(i)) + ", 0\n"
                notes_on.remove(i)"""
    
    for i in infile.split(" "):
        for j in i:
            if j not in notes_on:
                notes_on.append(j)
                outtext += "2, " + str(time_point) + ", Note_on_c, 0, " + str(ord(j)) + ", 100\n"
        for n in notes_on:
            if n not in i:
                notes_on.remove(n)
                outtext += "2, " + str(time_point) + ", Note_off_c, 0, " + str(ord(n)) + ", 0\n"
        
        time_point += step_size

    for n in notes_on:
        outtext += "2, " + str(time_point) + ", Note_off_c, 0, " + str(ord(n)) + ", 0\n"
        
    outtext += "2, " + str(time_point) + ", End_track\n0, 0, End_of_file\n"
    outfile.write(outtext)

for i in os.listdir("conv"):
    print i
    run("conv/" + i, "retCSV/" + i[:-4] + "csv")