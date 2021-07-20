#Ananagrams
import re
import time
start = time.time()
word_list = []
while True:
    line = input()
    if line == "": continue

    words = re.findall('([^\s]+)', line)
    if " ".join(words) == "#": break
    word_list.extend(words)

normalized_word_list = ["".join(sorted(w.upper())) for w in word_list]
# print(normalized_word_list)
ananagrams = []
anagrams_index = set()
for i in range(len(normalized_word_list)-1):
    if i in anagrams_index:
        continue
    anagram_found = False
    for j in range(i+1,len(normalized_word_list)):
        if normalized_word_list[i] == normalized_word_list[j]:
            anagrams_index.add(i)
            anagrams_index.add(j)
            anagram_found = True
    if not anagram_found:
        ananagrams.append(word_list[i])

if len(normalized_word_list)-1 not in anagrams_index: 
    ananagrams.append(word_list[len(normalized_word_list)-1])
ananagrams.sort()
# print(ananagrams)
print(*ananagrams, sep="\n")