dsu_root = []
dsu_size = []

def _union(x,y):
    x = _find(x)
    y = _find(y)

    if x == y: return

    if dsu_size[x] < dsu_size[y]:
        x,y = y,x

    dsu_root[y] = x
    dsu_size[x] = dsu_size[x] + dsu_size[y]

def _find(x):
    if x == dsu_root[x]:
        return x
    dsu_root[x] = _find(dsu_root[x])
    return dsu_root[x]

def _make_set(node_list):
    global dsu_root
    global dsu_size

    dsu_root = [x for x in node_list]
    dsu_size = [1]*len(node_list)

def check_connectedness(graph, node_list):
    _make_set(node_list)
    # import pdb; pdb.set_trace()
    for node in graph.keys():
        for neighbor in graph[node]:
            if _find(node) != _find(neighbor):
                _union(node,neighbor)
    
    return len(set(dsu_root)) == 1

def check_eulerian_cycle(degrees):
    return all([d%2 == 0 for d in degrees])

def solve(graph, degrees, node_count):
    if not check_eulerian_cycle(degrees): return False
    
    nodes = list(range(node_count))
    if not check_connectedness(graph, nodes): return False

    return True

def main():
    while True:
        try:
            n,r = [int(x) for x in input().split()]
            graph = {j:set() for j in range(n)}
            degrees = [0]*n
            for i in range(r):
                s,d = [int(x) for x in input().split()]
                graph[s].add(d)
                degrees[s] += 1
                degrees[d] += 1
            # print(graph, degrees)
            result = solve(graph,degrees,n)
            print(f"{'Possible' if result else 'Not Possible'}")
        except EOFError:
            break

if __name__ == "__main__":
    main()