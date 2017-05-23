#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 15:41:26 Shin Kanouchi

import argparse


def get_morphs(train_file):
    doc = list()
    sent = list()
    for line in open(train_file, encoding='utf-8'):
        if line.startswith('EOS') or line == "":
            doc.append(sent)
            sent = list()
            continue
        #print('chappy1--->' +line)
        #print('chappy2--->' + line.strip())
        #print(line.strip().split("\t"))
        surface, items = line.strip('\n').split('\t')
        #surface, items = line.strip().split('\t')
        #print('chappy4--->' + items)
        item_list = items.split(",")
        morph = {'surface': surface, 'base': item_list[6], 'pos': item_list[0], 'pos1': item_list[1]}
        sent.append(morph)
        #print(morph['surface'], morph['base'], morph['pos'], morph['pos1'])
    return doc

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.txt.mecab', help='input training data')
    args = parser.parse_args()
    my_morphs = get_morphs(args.train)
    #print(my_morphs)