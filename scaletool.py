notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
header = "  |  1           3           5           7           9                12                15          17          19          21"

class Guitar_String:
    def __init__(self, open_note, key):
        self.open_note = open_note
        self.key = key

    def build_scale(self):
        start_i = notes.index(self.key)
        scale = []
        scale.append(self.key)
        i = start_i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 1
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        i = i + 2
        scale.append(notes[i % len(notes)])
        return scale

    def build_string(self):
        sc = self.build_scale()
        output = ""
        if self.open_note in sc:
            if len(self.open_note) == 1:
                output = output + self.open_note + " "
            else:
                output = output + self.open_note
        else:
            output = output + "X "
        starting_note_index = notes.index(self.open_note)
        for x in range (1, 22):
            if notes[(x + starting_note_index) % len(notes)] in sc:
                f = Fret(notes[(x + starting_note_index) % len(notes)])
            else:
                f = Fret('X')
            output = output + str(f)
        return output


class Fret:
    def __init__(self, note):
        self.note = note
    
    def __str__(self):
        if(self.note == 'X'):
            return "|     "
        elif(len(self.note) == 2):
            return "|  " + self.note + " "
        else:
            return "|  " + self.note + "  "



def main():
    tuning = ['D', 'A', 'D', 'G', 'A', 'D']
    # tuning = ['E', 'A', 'D', 'G', 'B', 'E']
    my_key = 'F#'
    print(my_key + " Major Scale in " + "".join(tuning))    
    tuning.reverse()
    print(header)
    for t in range(len(tuning)):
        g = Guitar_String(tuning[t], my_key)
        print(g.build_string())
        line_break = "  "
        for z in range(0, 127):
            line_break = line_break + "-"
        print(line_break)
    

main()