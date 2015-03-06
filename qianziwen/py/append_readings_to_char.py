# coding: utf-8

import sys, os

root_dirname = os.path.dirname( os.path.dirname (os.path.dirname(__file__) ) )
sys.path.append( root_dirname )
from kanjiProcessor import *

def load_dict():
    dict_root_dirname = os.path.join(
        os.path.dirname(root_dirname),
        "dictionary"
        )
    input_dirname = os.path.join(
        os.path.join(dict_root_dirname, "unihan"),
        "dict"
        )
    return load_dictionaries(input_dirname)

def main():
    # load dict
    d = load_dict()
    # load
    dirname = os.path.join( os.path.dirname( os.path.dirname(__file__)), 'txt')
    input_filename = os.path.join(dirname, "1000_chars.txt")
    chars = load_file(input_filename)
    # process
    r = []
    for char in chars:
        r.append("%s\t%s" %(char, d.get(char, "").encode('utf8')))
    # output
    output_filename = os.path.join(dirname, "1000_chars.r.txt")
    #save_file(output_filename, r)
    save_file(output_filename, r)

if __name__ == '__main__':
    main()
