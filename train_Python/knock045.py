#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/10 18:39:23 Shin Kanouchi

import knock041
from collections import defaultdict


def main(all_sent):
    V_dict = defaultdict(list)
    for a_sent in all_sent:
        for a_chunk in a_sent:
            for another_chunk in a_sent:
                if a_chunk.num == another_chunk.dst:
                    V_yes = a_chunk.morphs_pos("動詞")
                    par = another_chunk.return_morphs_par()
                    if V_yes and par:
                        V_dict[a_chunk.return_Vbase()].append(par)
    return V_dict


def print_dict(V_dict):
    for k, Par_list in V_dict.items():
        print k, " ".join(set(Par_list))


if __name__ == '__main__':
    all_sent = knock041.make_morph("../data/neko.cabocha")
    V_dict = main(all_sent)
    print_dict(V_dict)
