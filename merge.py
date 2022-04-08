#!/usr/bin/env python3
import re

minLength = 8
maxLength = 25
input1 = open("input1.txt", "r", encoding="utf8")
input2 = open("input2.txt", "r", encoding="utf8")
list1 = input1.readlines()
list2 = input2.readlines()
list = []
dict = {}


def addListToDict(val):
    for word in val:
        word_length = len(word)
        if minLength <= word_length <= maxLength:
            dict[word] = True


print("Adding words from file 1")
addListToDict(list1)

print("Adding words from file 2")
addListToDict(list2)

print("Copying words from Dict to List")
for word in dict:
    list.append(word)

print("Sorting")
list.sort()

print("Exporting words to file")
with open("merge-output.txt", 'w', encoding="utf8") as file:
    for word in list:
        file.write(word)
