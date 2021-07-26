#!/usr/bin/env python3

# === Imports ===
import sys, argparse, itertools

# === Functions ===
def generator(chars, passrange, silent, output):

    for xs in itertools.product(chars, repeat=passrange):
        if not silent:
            print(''.join(xs))

        if output != None:
            with open(output, 'a') as f:
                f.write(''.join(xs) + '\n')

# === Main function ===
def main():
    # Variables
    version = 1.0
    chars = 'abcdefghijklmnopqrstuvwxyz'
    passwords = []
 
    parser = argparse.ArgumentParser(description='''
     █████        ██████  ████   ███           █████   
    ░░███        ███░░███░░███  ░░░           ░░███    
     ░███████   ░███ ░░░  ░███  ████   █████  ███████  
     ░███░░███ ███████    ░███ ░░███  ███░░  ░░░███░   
     ░███ ░███░░░███░     ░███  ░███ ░░█████   ░███    
     ░███ ░███  ░███      ░███  ░███  ░░░░███  ░███ ███
     ████████   █████     █████ █████ ██████   ░░█████ 
    ░░░░░░░░   ░░░░░     ░░░░░ ░░░░░ ░░░░░░     ░░░░░  
        ''', formatter_class=argparse.RawDescriptionHelpFormatter)

    # Arguments
    parser.add_argument('--version', action='version', version=f'%(prog)s {version}')
    parser.add_argument('-c', default=f'{chars}', help='set which characters will be used to create de wordlist. Default is the alphabet', dest='chars')
    parser.add_argument('-n', const='0123456789', action='store_const', help='use only %(const)s to create the wordlist',dest='chars')
    parser.add_argument('-l', type=int, help='set how much characters the words will have',dest='length')
    parser.add_argument('-r', nargs=2, type=int, help='set a range of numbers to be used as length', dest='range', metavar=('MIN', 'MAX'))
    parser.add_argument('-o', help='set an output file',dest='output') 
    parser.add_argument('-s', action='store_true', help="silent mode. Don't show the output", dest='silent')

    args = parser.parse_args()

    # Verifing word length and generating passwords
    if args.length == None and args.range == None:
        print("passwdgen.py: error: expected -l or -r argument")
        sys.exit(1)

    elif args.length != None:
        generator(args.chars, args.length, args.silent, args.output)

    else:
        for r in range(args.range[0], args.range[1] + 1):
            generator(args.chars, r, args.silent, args.output)


# === Call main ===
main()
