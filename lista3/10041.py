def solve(r, relatives):
    relatives.sort()
    size = len(relatives)
    if size % 2 == 0:
        median = (relatives[size//2] + relatives[size//2 - 1])//2
    else:
        median = relatives[size//2]
    # print(f"median: {median}")

    distance = 0
    for i in range(len(relatives)):
        distance += abs(median - relatives[i])
    
    return distance


def main():
    line_count = int(input())
    for i in range(line_count):
        case = [int(x) for x in input().split(" ")]
        r, relatives = case[0],case[1:]
        # print(f"distance: {solve(r,relatives)}\n")
        print(solve(r,relatives))

if __name__ == "__main__":
    main()