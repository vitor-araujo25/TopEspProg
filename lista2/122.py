#Trees on the level
from sys import stdin
import re
from collections import defaultdict

PATTERN = re.compile("\((\d+),(\w*)\)")

def evaluate(token_tree):
    found_paths = set()
    levels = defaultdict(list)
    for token in token_tree:
        node = PATTERN.findall(token)[0] # tupla ('num','pos?')
        path = node[1]
        if path in found_paths:
            return
        found_paths.add(path)
        levels[len(path)].append(node)
       
    bfs_order = []
    for level in sorted(levels.keys()):
        levels[level].sort(key=lambda x: x[1])
        for node in levels[level]:
            value, path = node
            if path[:-1] in found_paths:
                bfs_order.append(value)      
            else:
                return
    
    return bfs_order

def build_output(evaluated_input):
    if evaluated_input is None:
        print("not complete")
    else:
        print(*evaluated_input,sep=" ")

def main():
    tree = []
    for line in stdin:
        elements = line.strip().split(" ")
        tree.extend(elements)
        if elements[-1] == "()":
            build_output(evaluate(tree[:-1]))
            tree = []
        

if __name__ == "__main__":
    main()