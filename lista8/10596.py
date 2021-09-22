def _union():
    pass

def _find():
    pass

def _make_set():
    pass

def check_connectedness():
    pass

def check_eulerian_cycle(degrees):
    return sum(degrees) % 2 == 0

def solve(graph, degrees, node_count):
    if not check_eulerian_cycle(degrees): return False
    
    nodes = list(range(node_count))
    if not check_connectedness(graph, nodes): return False

    return True

    

def main():
    while True:
        try:
            n,r = [int(x) for x in input().split()]
            graph = {j:list() for j in range(n)}
            degrees = [0]*n
            for i in range(r):
                s,d = [int(x) for x in input().split()]
                graph[s].append(d)
                graph[d].append(s)
                degrees[s] += 1
                degrees[d] += 1
            result = solve(graph,degrees,n)
            print(f"{'Possible' if result else 'Not Possible'}")
        except EOFError:
            break

if __name__ == "__main__":
    main()