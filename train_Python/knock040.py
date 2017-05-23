#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/01 22:05:30 Shin Kanouchi


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

def make_morph(cabo_file):
    all_sent = []
    one_sent = []
    for line in open(cabo_file, encoding='utf-8'):
        if "　" in line:    #if "\t" in line:
            print(line)
            surf, item = line.strip("\n").split("　")
            #surf, item = line.strip("\n").split("\t")
            items = item.split(",")
            print(items)
            one_sent.append(Morph(surf, items[6], items[0], items[1]))
        elif "EOS" in line:
            #print(line)
            all_sent.append(one_sent)
            one_sent = []
    print(all_sent)
    for item in all_sent[3]:
        print('surface=%s\tbase=%s\tpos=%s\tpos1=%s' %
        (item.surface, item.base, item.pos, item.pos1))

if __name__ == '__main__':
    make_morph("../data/neko.txt.cabocha")