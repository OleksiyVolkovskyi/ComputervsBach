import os

def run(inpath, outpath):
    infile = open(inpath).read().split("\n")
    outfile = open(outpath, "w")
    outtext = ""

    step_size = 1
    last_time_point = 0

    notes_on = []
    
    ot = []
    
    for line_number, line in enumerate(infile):
        if line:
            line = line.replace(" ", "").split(",")

            if line[2].lower() in ["note_off_c", "note_on_c", "control_c"]:
                line = line[1:]
                    
                time_point, command, instrument, note, volume = line
                time_point = int(time_point)
                instrument = int(instrument)
                note = int(note)
                volume = int(volume)
                
                if command.lower() == "note_off_c":
                    note_on = False
                elif command.lower() == "control_c":
                    note_on = False
                elif volume == 0:
                    note_on = False
                else:
                    note_on = True
                
                if note_on:
                    if note not in notes_on:
                        notes_on.append(note)
                else:
                    if note in notes_on:
                        notes_on.remove(note)
                
                if time_point != last_time_point:
                    td = time_point - last_time_point
                    td /= step_size
                    eed = []
                    for n in notes_on:
                        eed.append(chr(n))
                    ed = " ".join(eed * td)
                    ot.append(ed)
                                
                last_time_point = time_point
                
                if command.lower() == "control_c":
                    for i in notes_on:
                        notes_on.remove(i)
            
    outfile.write(" ".join(ot))

for i in os.listdir("CSV"):
    print i
    run("CSV/" + i, "CUST/" + i[:-3] + "cust")