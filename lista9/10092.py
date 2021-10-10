import math
from copy import deepcopy
from collections import defaultdict

def bfs(graph,s,t):
    parent = [-1 for _ in range(len(graph))]
    queue = [(s,math.inf)]
    parent[s] = -2

    while len(queue) != 0:
        current_node, flow = queue.pop(0)
        for neighbor, remaining_capacity in graph[current_node].items():
            if remaining_capacity > 0 and parent[neighbor] == -1:
                parent[neighbor] = current_node
                new_flow = min(flow, remaining_capacity)
                if neighbor == t:
                    return new_flow, parent
                queue.append((neighbor, new_flow))

    return 0, parent

def solve(graph, source, sink):
    max_flow = 0
    while True:
        flow, parent = bfs(graph, source, sink)
        if flow == 0:
            break
        max_flow += flow
        current = sink
        while current != source:
            prev = parent[current]
            graph[prev][current] -= flow
            graph[current][prev] += flow
            current = prev

    return max_flow

def main():
    while True:
        n_categories, n_problems = [int(x) for x in input().split()]
        if (n_categories, n_problems) == (0,0):
            break
        problem_count = [int(x) for x in input().split()]

        # [0,n_problems) -> problemas
        # [n_problems, n_problems + n_categories) -> categorias
        # n_problems + n_categories -> source
        # n_problems + n_categories + 1 -> sink

        cap = defaultdict(dict)

        categories_offset = n_problems
        source = n_problems + n_categories
        sink = source + 1

        for i in range(n_problems):
            cap[source][i] = 1
            cap[i][source] = 0
        for i in range(n_categories):
            cap[categories_offset + i][sink] = problem_count[i]
            cap[sink][categories_offset + i] = 0

        problem = 0
        while problem < n_problems:
            line = [int(x) for x in input().split()]
            categories_len = line[0]
            while categories_len == len(line[1:categories_len+1]):
                for category in line[1:categories_len+1]:
                    category -= 1
                    cap[problem][categories_offset + category] = 1
                    cap[categories_offset + category][problem] = 0
                problem += 1
                line = line[categories_len+1:]
                try:
                    categories_len = line[0]
                except IndexError:
                    break

        original = deepcopy(cap)
        max_flow = sum(problem_count)

        flow = solve(cap, source, sink)

        if flow == max_flow:
            print(1)
            for i in range(n_categories):
                count = 0
                for j in range(n_problems):
                    new_i = categories_offset + i
                    if new_i in original[j] and original[j][new_i] == 1 and cap[j][new_i] == 0:
                        if count != 0:
                            print(" ", end="")
                        print(f"{j+1}", end="")
                        count += 1
                print()
        else:
            print(0)


if __name__ == "__main__":
    main()