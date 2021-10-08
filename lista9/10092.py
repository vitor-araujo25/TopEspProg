def solve(graph, source, sink):
    pass

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
        total_nodes = n_categories + n_problems + 2
        graph = [[0 for _ in range()] for _ in range(total_nodes)]
        categories_offset = n_problems
        source = n_problems + n_categories
        sink = source + 1

        graph[source] = [1 if i < n_problems else 0 for i in range(total_nodes)]
        for i in range(len(problem_count)):
            graph[categories_offset + i][sink] = problem_count[i]

        for i in range(n_problems):
            categories_for_problem_i = [int(x)-1 for x in input().split()]
            for category in categories_for_problem_i:
                graph[i][category] = 1

        max_flow = sum(problem_count)

        flow = solve(graph, source, sink)

        if flow == max_flow:
            print(1)
            #...
        else:
            print(0)


if __name__ == "__main__":
    main()