import math

def _dijkstra(n,source,target,graph):
    distances = [math.inf for _ in range(n)]
    distances[source] = 0

    queue = [source]

    while len(queue) > 0:
        current = queue[0]
        for dest, time in enumerate(graph[current]):
            updated_distance = distances[current] + time + 60
            if distances[dest] > updated_distance:
                distances[dest] = updated_distance
                queue.append(dest)

        queue.pop(0)
    return distances[target]

def solve(target, timings, elevators):
    graph = [[math.inf for j in range(100)] for i in range(100)]
    
    for i,floors in enumerate(elevators):
        for j,floor in enumerate(floors):
            for k in range(j+1,len(floors)):
                d = abs(floors[k] - floor)*timings[i]
                if d < graph[floor][floors[k]]:
                    graph[floor][floors[k]] = d
                    graph[floors[k]][floor] = d

    return _dijkstra(100, 0, target, graph)


def get_input():
    return list(map(int, input().split()))

def main():
    while True:
        try:
            n,k = get_input()
            timings = get_input()
            elevator_floors = []
            for _ in range(n):
                elevator_floors.append(get_input())

            distance = solve(k, timings, elevator_floors)

            if distance == math.inf:
                print("IMPOSSIBLE")
            elif distance == 0:
                print(0)
            else:
                print(distance-60)
        except EOFError:
            break

if __name__ == "__main__":
    main()