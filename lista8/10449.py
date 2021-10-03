import math

class Edge:
    def __init__(self, source, destination, cost):
        self.source = source
        self.target = destination
        self.weight = cost

def bellman_ford(source, edge_list, node_count):
    distances = [math.inf for _ in range(node_count)]
    distances[source] = 0

    for _ in range(node_count-1):
        update = False

        for edge in edge_list:
            candidate_distance = distances[edge.source] + edge.weight
            if candidate_distance < distances[edge.target]:
                distances[edge.target] = candidate_distance
                update = True
        
        if not update: break
    
    for edge in edge_list:
        if distances[edge.source] + edge.weight < distances[edge.target]:
            distances[edge.target] = -math.inf

    return distances


def main():
    count = 1
    while True:
        try:
            first_row = [int(x) for x in input().strip().split() if x != ""]
            n = first_row[0]
            busynesses = first_row[1:]
            roads = int(input().strip())
            edges = []
            distances = []
            if len(busynesses) != 0:
                for _ in range(roads):
                    u,v = [int(x) for x in input().strip().split() if x != ""]
                    u -=1
                    v -=1
                    cost = busynesses[v] - busynesses[u]
                    edges.append(Edge(u,v,cost**3))
            
                distances = bellman_ford(0, edges, len(busynesses))
            
            q = int(input().strip())
            print(f"Set #{count}")
            count += 1
            
            for _ in range(q):
                try:
                    target = int(input().strip())
                    target -= 1
                    if distances[target] < 3 or distances[target] == math.inf: 
                        print("?")
                    else: 
                        print(distances[target])
                except IndexError:
                    break
        except EOFError:
            break
        except:
            continue 
    
if __name__ == "__main__":
    main()