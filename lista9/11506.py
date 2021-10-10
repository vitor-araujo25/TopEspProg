import math

M = 0
W = 0

def bfs(graph,s,t):
    visited = [False for _ in range(len(graph))]
    queue = [s]
    visited[s] = True

    prev = [None for _ in range(len(graph))]

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == t:
            break
        for neighbor, remaining_capacity in enumerate(graph[current_node]):
            if remaining_capacity > 0 and not visited[neighbor]:
                visited[neighbor] = True
                prev[neighbor] = current_node 
                queue.append(neighbor)

    if prev[t] == None: return 0

    max_flow = math.inf
    current = t
    previous = prev[t]
    while previous != None:
        max_flow = min(max_flow, graph[previous][current])
        current = previous
        previous = prev[current]
    
    current = t
    previous = prev[t]
    while previous != None:
        graph[previous][current] -= max_flow
        graph[current][previous] += max_flow
        current = previous
        previous = prev[current]

    return max_flow

def solve(graph, source, sink):
    max_flow = 0
    flow = 1
    while flow != 0:
        flow = bfs(graph, source, sink)
        max_flow += flow
    
    return max_flow

def get_machine_shadow_node(machine):
    return machine+M

def main():
    global M,W
    while True:
        M, W = [int(x) for x in input().split()]
        if (M,W) == (0,0):
            break    
        
        s = 0
        t = M-1
        shadow_s=get_machine_shadow_node(s)
        shadow_t=get_machine_shadow_node(t)

        N = 2*M
        graph = [[0 for _ in range(N)] for _ in range(N)]
        graph[s][shadow_s], graph[t][shadow_t] = math.inf, math.inf

        for _ in range(M-2):
            line = [int(x) for x in input().split()]
            machine, cost = line[0]-1, line[1]
            shadow_node = get_machine_shadow_node(machine)
            
            graph[machine][shadow_node] = cost


        for _ in range(W):
            u,v,cost = [int(x) for x in input().strip().split() if x != ""]
            u -= 1
            v -= 1

            shadow_u = get_machine_shadow_node(u)
            shadow_v = get_machine_shadow_node(v)

            graph[shadow_u][v], graph[shadow_v][u] = cost, cost


        max_flow = solve(graph, s, shadow_t)

        # print(f"Network {count}")
        print(f"{max_flow}")
        # count += 1


if __name__ == "__main__":
    main()


