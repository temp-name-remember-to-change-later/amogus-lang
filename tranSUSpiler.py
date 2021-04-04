import sys
import getopt

def help():
    print('''Usage: tranSUSpiler [options] <file>
Converts text file into sus amogus text, or decodes it.
If neither of -s or -n are passed, defaylts to encoding

Arguments:
    -f               Specify input file name
    -h, --help       Show this extremely helpful help screen
    -s, --sus        Convert to sus amogus text
    -n, --not-sus    Convert to non-sus regular text
''')

def print_usage():
    print('Usage: tranSUSpiler [options] -f <file>')

def parse_args(argv):
    fname = ''
    mode = ''
    try:
        opts, _ = getopt.getopt(argv, 'hsnf:')
    except getopt.GetoptError:
        print_usage()
        exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
        elif opt == '-f':
            fname = arg
        elif opt in ('-s', '--sus'):
            mode = 'sus'
        elif opt in ('-n', '--not-sus'):
            if mode == 'sus':
                print_usage()
                exit(1)
            else:
                mode = 'not-sus'
    if mode == '':
        mode = 'sus'
    if fname == '':
        print_usage()
        exit(1)
    return fname, mode
    
# dictionaries
english_to_amogus = {
        '0': 'amogus',
        '1': 'Amogus',
        '2': 'aMogus',
        '3': 'AMogus',
        '4': 'amOgus',
        '5': 'AmOgus',
        '6': 'aMOgus',
        '7': 'AMOgus',
        '8': 'amoGus',
        '9': 'AmoGus',
        'a': 'aMoGus',
        'b': 'AMoGus',
        'c': 'amOGus',
        'd': 'AmOGus',
        'e': 'aMOGus',
        'f': 'AMOGus',
        'g': 'amogUs',
        'h': 'AmogUs',
        'i': 'aMogUs',
        'j': 'AMogUs',
        'k': 'amOgUs',
        'l': 'AmOgUs',
        'm': 'aMOgUs',
        'n': 'AMOgUs',
        'o': 'amoGUs',
        'p': 'AmoGUs',
        'q': 'aMoGUs',
        'r': 'AMoGUs',
        's': 'amOGUs',
        't': 'AmOGUs',
        'u': 'aMOGUs',
        'v': 'AMOGUs',
        'w': 'amoguS',
        'x': 'AmoguS',
        'y': 'aMoguS',
        'z': 'AMoguS',
        'A': 'amOguS',
        'B': 'AmOguS',
        'C': 'aMOguS',
        'D': 'AMOguS',
        'E': 'amoGuS',
        'F': 'AmoGuS',
        'G': 'aMoGuS',
        'H': 'AMoGuS',
        'I': 'amOGuS',
        'J': 'AmOGuS',
        'K': 'aMOGuS',
        'L': 'AMOGuS',
        'M': 'amogUS',
        'N': 'AmogUS',
        'O': 'aMogUS',
        'P': 'AMogUS',
        'Q': 'amOgUS',
        'R': 'AmOgUS',
        'S': 'aMOgUS',
        'T': 'AMOgUS',
        'U': 'amoGUS',
        'V': 'AmoGUS',
        'W': 'aMoGUS',
        'X': 'AMoGUS',
        'Y': 'amOGUS',
        'Z': 'AmOGUS',
        ' ': 'ඞ',
        'ඞ': 'ඞඞ' }
amogus_to_english = {v: k for k, v in english_to_amogus.items()}

# make characters sus
# ignores non-alphanumeric characters and strings longer than a character
def ensus(c):
    if c in english_to_amogus.keys():
        return english_to_amogus[c]
    else:
        return c

# makes sus characters non-sus
# ignores anything not in the correct format of aMoGuS
def desus(sus):
    if sus in amogus_to_english.keys():
        return amogus_to_english[sus]
    else:
        return sus

def main(argv):
    fname, mode = parse_args(argv)
    if mode == 'sus':
        f = open(fname, 'r', encoding='utf-8')
        outfname = fname + '.sus'
        outf = open(outfname, 'wb')
        for line in f:
            for ch in line:
                outf.write(ensus(ch).encode('utf-8'))
                if ch != '\n':
                    outf.write(' '.encode('utf-8'))
        outf.close()
    elif mode == 'not-sus':
        if not fname.endswith('.sus'):
            print('Error: file to decode must have the extension .sus')
            exit(2)
        f = open(fname, 'r', encoding='utf-8')
        outfname = fname[:len(fname) - 4]
        outf = open(outfname, 'wb')
        for line in f:
            arr = []
            for ch in line:
                if ch == ' ':
                    outf.write(desus(''.join(arr)).encode('utf-8'))
                    arr = []
                else:
                    arr.append(ch)
            outf.write('\n'.encode('utf-8'))
        outf.close()

    else:
        print_usage()
        exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
