for _ in range(int(input())):
    n, m = [int(x) for x in input().strip().split() if x != ""]
    graph = [-1] * n

    for i in range(m):
        u, v = [int(x) for x in input().strip().split() if x != ""]
        u -= 1
        v -= 1

        while graph[u] >= 0:
            u = graph[u]

        while graph[v] >= 0:
            v = graph[v]

        if u == v:
            continue

        if u > v:
            u, v = v, u

        graph[u] = graph[u] + graph[v]
        graph[v] = u

    print(-min(graph))