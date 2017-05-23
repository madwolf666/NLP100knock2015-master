#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/14 11:18:00 Shin Kanouchi
import random

my_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
my_list = []
words = my_text.split()
for word in words:
    if len(word) <= 4:
        my_list.append(word)
    else:
        body = word[1:-1]
        body_list = list(body)
        random.shuffle(body_list)
        new_body = "".join(body_list)
        new_word = "%s%s%s" % (word[0], new_body, word[-1])
        my_list.append(new_word)
print(" ".join(my_list))