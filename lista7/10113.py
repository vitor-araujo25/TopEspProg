import re
from collections import defaultdict, deque
import math

ASSERTION_PATTERN = re.compile("(\d+) (\w+) = (\d+) (\w+)")
QUERY_PATTERN = re.compile("(\w+) = (\w+)")

graph = defaultdict(list)

def reduce_rate(a,b):
    gcd = math.gcd(a,b)
    return (a // gcd, b // gcd)

def combine_rates(rate1, rate2):
    a1, b1 = rate1
    a2, b2 = rate2
    new_rate = (a1*a2, b1*b2)
    if new_rate[0] > 9000 or new_rate[1] > 9000:
        new_rate = reduce_rate(*new_rate)
    return new_rate

def add_information(amount_a, a, amount_b, b):
    amount_a, amount_b = reduce_rate(amount_a, amount_b)
    graph[a].append((b, amount_a, amount_b))
    graph[b].append((a, amount_b, amount_a))

def _bfs(source, goal, visited):
    queue = deque()
    queue.appendleft((source,1,1))
    visited.add(source)
    while queue:
        
        current, prev_amount_a, prev_amount_b = queue.pop()

        for node_name, amount_a, amount_b in graph[current]:
            if node_name not in visited:
                if node_name == goal:
                    final_a, final_b = combine_rates((amount_a,amount_b),(prev_amount_a,prev_amount_b))
                    return final_a, final_b
                path_amount_a, path_amount_b = combine_rates((amount_a,amount_b),(prev_amount_a,prev_amount_b))
                queue.appendleft((node_name,path_amount_a,path_amount_b))
                visited.add(node_name)
    
    return

def run_query(a,b):
    values = _bfs(a,b,set())
    if values:
        return values
    else:
        return None, None

def main():
    while True:
        data = input().strip()
        if data == ".":
            break
        if data[0] == "!":
            assertion = ASSERTION_PATTERN.search(data)
            amount_a, a, amount_b, b = assertion.groups()
            add_information(int(amount_a), a, int(amount_b), b)
        else:
            query = QUERY_PATTERN.search(data)

            a, b = query.groups()
            amount_a, amount_b = run_query(a,b)
            if (amount_a, amount_b) != (None, None):
                amount_a, amount_b = reduce_rate(amount_a, amount_b)
            else:
                amount_a, amount_b = "?", "?"
            print(f"{amount_a} {a} = {amount_b} {b}")

    # print(graph)
if __name__ == "__main__":
    main()