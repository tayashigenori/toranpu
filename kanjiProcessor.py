# coding: utf-8

import os
import re

def load_file(filename):
    r = []
    f = open(filename, 'r')
    try:
        for line in f.readlines():
            r.append(unicode(line.rstrip(), 'utf8'))
    finally:
        f.close()
    return r

def save_file(filename, lines, require_encode = True, require_rstrip = True):
    r = []
    f = open(filename, 'w')
    try:
        for line in lines:
            if require_rstrip:
                line = line.rstrip()
            if require_encode:
                line = line.encode('utf8')
            f.write(line + "\n")
    finally:
        f.close()
    return

def line_to_char(lines, skip_chars = [u" ", u"　"]):
    r = []
    for line in lines:
        line = unicode(line.strip(), 'utf8')
        r += [char for char in line if char not in skip_chars]
    return r

def load_dictionaries(dirname):
    d = {}
    for i in range(1, 65):
        filename = os.path.join(dirname, "%s.txt" %i)
        d.update( load_dictionary(filename) )
    return d

def load_dictionary(filename):
    d = {}
    f = open(filename)
    try:
        for line in f.readlines():
            line = unicode(line.rstrip(), 'utf8')
            pat = re.compile(u',(?={)')
            (kanji, readings) = re.split(pat, line)
            d[kanji] = readings
    finally:
        f.close()
    return d
