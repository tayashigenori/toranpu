# coding: utf-8

import sys, os

sys.path.append(os.path.dirname( os.path.dirname (os.path.dirname(__file__) ) ) )
from kanjiProcessor import *

def main():
    dirname = os.path.join( os.path.dirname( os.path.dirname(__file__)), 'txt')
    # load
    input_filename = os.path.join(dirname, "125_lines.txt")
    lines = load_file(input_filename)
    # process
    chars = line_to_char(lines)
    # output
    output_filename = os.path.join(dirname, "1000_chars.txt")
    save_file(output_filename, chars)

if __name__ == '__main__':
    main()
