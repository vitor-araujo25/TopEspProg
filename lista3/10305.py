#Ordering Tasks

def find_sources(graph):
    sources = [node for node, incidents in graph.items() if len(incidents) == 0]
    return sorted(sources)

def topological_sort(graph, total_nodes):
    visited = []
    # visiting_idx = 0
    while True:
        current_sources = find_sources(graph)
        if len(current_sources) == 0: break
        visited.extend(current_sources)
        for source in current_sources:
            # source = visited[visiting_idx]
            del graph[source]
            for node, incidents in graph.items():
                if source in incidents:
                    incidents.remove(source)
    
    return visited

def main():
    while True:
        try:
            total_nodes, total_edges = [int(x) for x in input().split(" ")]
            if total_nodes == 0 and total_edges == 0:
                return
            reverse_adj_list = {i:set() for i in range(1,total_nodes+1)}
            for _ in range(total_edges):
                i,j = [int(x) for x in input().split(" ")]
                reverse_adj_list[j].add(i)
            # print(reverse_adj_list)
            ans = topological_sort(reverse_adj_list, total_nodes)
            print(" ".join([str(i) for i in ans]))
        except EOFError:
            return
        
if __name__ == "__main__":
    main()