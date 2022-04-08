#!/usr/bin/env python3
import re

input1 = open("input1.txt", "r", encoding="utf8")
input2 = open("input2.txt", "r", encoding="utf8")
list1 = input1.readlines()
list2 = input2.readlines()
list = []
dict = {}

print("Adding words from file 1")
for word in list1:
    word_len = len(word)
    if (word_len >= 8 and word_len <= 25):
        dict[word] = True

print("Adding words from file 2")
for word in list2:
    word_len = len(word)
    if (word_len >= 8 and word_len <= 25):
        dict[word] = True

print("Copying words from Dict to List")
for word in dict:
    list.append(word)

print(len(list))

print("Sorting")
list.sort()

print("Exporting words to file")
with open("output3.txt", 'w', encoding="utf8") as file:
    for row in list:
        file.write(row)