#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/15 17:55:39 Shin Kanouchi

import argparse


def main(n, my_text):
    my_list1 = []
    for line in open(my_text):
        my_list1.append(line.strip())

    for i in range(n):
        print my_list1[i]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', dest='N', default=5)
    parser.add_argument('-t', '--train', dest='train', default="../data/hightemp.txt", help='input training data')
    args = parser.parse_args()
    main(int(args.N), args.train)
