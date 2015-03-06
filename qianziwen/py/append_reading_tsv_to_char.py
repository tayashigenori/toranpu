# coding: utf-8

import sys, os
import json

sys.path.append(os.path.dirname( os.path.dirname (os.path.dirname(__file__) ) ) )
from kanjiProcessor import *

def main():
    # load
    dirname = os.path.join( os.path.dirname( os.path.dirname(__file__)), 'txt')
    input_filename = os.path.join(dirname, "1000_chars.r.txt")
    lines = load_file(input_filename)
    # process
    r = []
    for line in lines:
        char, reading = line.split(u"\t")
        reading_d = json.loads(reading)
        r.append("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"
                 %(char,
                   reading_d.get("kMandarin", ""),
                   reading_d.get("kCantonese", ""),
                   reading_d.get("kJapaneseOn", ""),
                   reading_d.get("kHangul", ""),
                   reading_d.get("kKorean", ""),
                   reading_d.get("kVietnamese", ""),
                   reading_d.get("kTang", "")
                   )
                 )
    # output
    output_filename = os.path.join(dirname, "1000_chars.r.tsv")
    save_file(output_filename, r, True, False)

if __name__ == '__main__':
    main()
