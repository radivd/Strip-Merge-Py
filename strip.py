#!/usr/bin/env python3
import re

my_file = open("input.txt", "r", encoding="utf8")
content = my_file.readlines()
list = []
dict = {}
processed = 0
added = 0

for word in content:
    newWord = re.sub(r'[\W+/g]+', '', word.lower())
    newWordLen = len(newWord)
    processed += 1
    if (newWordLen >= 8 and newWordLen <= 25 and re.search(r'[^æøåÆØÅa-zA-Z]', newWord) == None):
        dict[newWord] = True
        added += 1
    print("Processed " + str(processed) + " Added " + str(added))

print("Copying words from Dict to List")
for word in dict:
    list.append(word)

print("Sorting List")
list.sort()

print("Exporting list to txt")
with open("output.txt", 'w', encoding="utf8") as file:
    for row in list:
        file.write(row + '\n')