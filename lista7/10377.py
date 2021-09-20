import sys

states = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
}

directions = 'NESW'

def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        try:
            n_row, n_col = list(map(int, next(recs).split()))
            maze = [next(recs) for _ in range(n_row)]
            x0, y0 = list(map(int, next(recs).split()))

            cmds = []
            while True:
                data = next(recs).split()
                if not data:
                    raise GeneratorExit
                cmds.extend(data)

        except (GeneratorExit, StopIteration):
            x, y = x0 - 1, y0 - 1
            direction = 0
            state = states[directions[direction]]

            cmds = "".join(cmds)
            for cmd in cmds:

                if cmd == 'R':
                    direction = (direction + 1) % 4
                    state = states[directions[direction]]
                
                elif cmd == 'L':
                    direction = (direction - 1) % 4
                    state = states[directions[direction]]

                elif cmd == 'F':
                    x1, y1 = x + state[0], y + state[1]
                    if (0 <= x1 < n_row and 0 <= y1 < n_col and
                                maze[x1][y1] == ' '):
                        x, y = x1, y1
                
                elif cmd == 'Q':
                    print(f"{x + 1} {y + 1} {directions[direction]}")
                    if tdx != n_case - 1:
                        print()

if __name__ == '__main__':
    main()