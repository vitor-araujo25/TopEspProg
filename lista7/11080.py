import sys
from collections import deque


def bipartite_graph(graph, n_node, n_edge):
    if n_edge == 0:
        return n_node

    colors = [-1] * n_node
    visited = [False] * n_node
    n_colors = [0] * 2

    stack = deque([0])
    visited[0] = True
    colors[0] = 0
    n_colors[0] = 1
    n_guard = 0

    while stack:
        curr = stack.pop()
        for child in graph[curr]:
            if not visited[child]:
                visited[child] = True
                stack.append(child)
                colors[child] = 1 - colors[curr]
                n_colors[colors[child]] += 1
            else:
                if colors[child] >= 0 and colors[child] != 1 - colors[curr]:
                    return -1

        if not stack:
            
            if n_colors[0] and not n_colors[1]:
                n_guard += n_colors[0]
            elif not n_colors[0] and n_colors[1]:
                n_guard += n_colors[1]
            else:
                n_guard += min(n_colors)

            n_colors[0] = 0
            n_colors[1] = 0

            for idx, v in enumerate(visited):
                if not v:
                    stack.append(idx)
                    visited[idx] = True
                    colors[idx] = 0
                    n_colors[0] = 1
                    break

    return n_guard


def main():
    recs = iter(sys.stdin.readlines())

    n_case = int(next(recs))
    for _ in range(n_case):
        n_node, n_edge = list(map(int, next(recs).split()))
        
        graph = [[] for _ in range(n_node)]

        for _ in range(n_edge):
            src, tgt = list(map(int, next(recs).split()))
            graph[src].append(tgt)
            graph[tgt].append(src)

        print("{}".format(bipartite_graph(graph, n_node, n_edge)))

if __name__ == '__main__':
    main()