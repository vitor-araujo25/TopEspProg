import math

class Edge:
    def __init__(self, source, destination, capacity):
        self.s = source
        self.t = destination
        self.cap = capacity
        self.flow = 0
        self.residual = None
    
    def is_residual(self):
        return self.cap == 0
    
    def remaining_capacity(self):
        return self.cap - self.flow
    
    def augment(self, incoming_flow):
        self.flow += incoming_flow
        self.residual.flow -= incoming_flow

def bfs(graph,s,t):
    visited = [False for _ in range(len(graph))]
    queue = [s]
    visited[s] = True

    prev = [None for _ in range(len(graph))]

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == t:
            break
        for target, edge in graph[current_node].items():
            if edge.remaining_capacity() > 0 and not visited[edge.t]:
                visited[edge.t] = True
                prev[edge.t] = edge
                queue.append(edge.t)

    if prev[t] == None: return 0

    max_flow = math.inf
    edge = prev[t]
    while edge != None:
        max_flow = min(max_flow, edge.remaining_capacity())
        edge = prev[edge.s]
    
    edge = prev[t]
    while edge != None:
        edge.augment(max_flow)
        edge = prev[edge.s]

    return max_flow

def solve(graph, source, sink):
    max_flow = 0
    flow = 1
    while flow != 0:
        flow = bfs(graph, source, sink)
        max_flow += flow
    
    return max_flow

def main():
    count = 1
    while True:
        n = int(input())
        if n == 0:
            break    
        
        s,t,edge_count = [int(x) for x in input().strip().split() if x != ""]

        s -= 1
        t -= 1
        
        graph = [dict() for _ in range(n)]

        for _ in range(edge_count):
            u,v,bw = [int(x) for x in input().strip().split() if x != ""]
            u -= 1
            v -= 1

            if v in graph[u]:
                graph[u][v].cap += bw
                graph[v][u].cap += bw
            else:
                edge1 = Edge(u,v,bw)
                edge2 = Edge(v,u,bw)
                res1 = Edge(v,u,0)
                res2 = Edge(u,v,0)
                edge1.residual, res1.residual = res1, edge1
                edge2.residual, res2.residual = res2, edge2
                graph[u][v] = edge1
                graph[v][u] = edge2
        
        max_flow = solve(graph, s, t)

        print(f"Network {count}")
        print(f"The bandwidth is {max_flow}.\n")
        count += 1


if __name__ == "__main__":
    main()


