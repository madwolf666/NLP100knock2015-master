#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/04/13 19:39:23 Shin Kanouchi

str1  = u"パタトクカシーー"
str_list = [str1[0], str1[2], str1[4], str1[6]]
print(str_list)
print("".join(str_list).encode('utf-8'))