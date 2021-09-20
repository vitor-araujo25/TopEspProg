from sys import stdin
from collections import defaultdict

def solve(tree: defaultdict, node_set: defaultdict, case_idx: int):
    result = True if len(node_set) == 0 else _solve(tree, node_set)
    print(f"Case {case_idx} is{'' if result else ' not'} a tree.")

def _solve(tree: defaultdict, incoming_edges: defaultdict):
    root = -1
    # print(incoming_edges)
    for node, count in incoming_edges.items():
        if count == 0 and root == -1:
            root = node
        elif count == 0 and root != -1:
            return False
        elif count != 1:
            return False

    visited = {key:False for key in incoming_edges.keys()}

    # print(tree, root)
    dfs(tree, root, visited)
    # print(visited)

    for node, was_visited in visited.items():
        if was_visited == False:
            return False
    
    return True


def dfs(tree, root, visits_map):
    visits_map[root] = True
    for child in tree[root]:
        if visits_map[child] == False:
            dfs(tree, child, visits_map)

def main():
    edges = defaultdict(list)
    incoming_edges = dict()
    i = 1
    for line in stdin:
        inputs = [int(x) for x in line.strip().split() if x != ""]
        for j in range(0, len(inputs)-1, 2):
            a,b = inputs[j], inputs[j+1]
            if (a,b) == (-1,-1):
               break 
            elif (a,b) == (0,0):
                solve(edges, incoming_edges, i)
                edges = defaultdict(list)
                incoming_edges = dict()
                i += 1
            else:
                edges[a].append(b)
                if a not in incoming_edges.keys():
                    incoming_edges[a] = 0
                if b not in incoming_edges.keys():
                    incoming_edges[b] = 1
                else:
                    incoming_edges[b] += 1

if __name__ == "__main__":
    main()