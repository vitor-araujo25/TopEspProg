#Ananagrams
import re
from collections import Counter 

word_list = []
while True:
    line = input()
    if line == "": continue

    words = re.findall('([^\s]+)', line)
    if " ".join(words) == "#": break
    word_list.extend(words)

normalized_word_list = [w.upper() for w in word_list]
counter = Counter()
    