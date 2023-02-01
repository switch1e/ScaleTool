header = "  |  1           3           5           7           9                12                15          17          19          21"
from guitar import *


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