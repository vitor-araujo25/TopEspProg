import sys

sys.setrecursionlimit(20000)
spreadsheet = []

def _is_calculated(i,j):
    return spreadsheet[i][j][0] != "="

def _convert_column(col):
    size = len(col)
    col[0]
    if size == 1:
        return ord(col[0]) - ord("A")
    if size == 2:
        return 26*(ord(col[0]) - ord("A") + 1) + (ord(col[1]) - ord("A"))
    if size == 3:
        return 26*26*(ord(col[0]) - ord("A") + 1) + 26*(ord(col[1]) - ord("A") + 1) + (ord(col[2]) - ord("A"))

def parse_formula(formula):
    cell_names = formula[1:].split("+")
    terms = []
    for name in cell_names:
        i = 0
        while ord(name[i]) - ord("A") >= 0:
            i += 1
        
        column = _convert_column(name[:i])
        row = int(name[i:])-1
        terms.append((row,column))
        
    return terms

def compute(i,j):
    global spreadsheet
    #list of (i,j) pairs
    if _is_calculated(i,j): 
        return spreadsheet[i][j]
    terms = parse_formula(spreadsheet[i][j])
    values = []
    for term in terms:
        if _is_calculated(*term): 
            values.append(spreadsheet[term[0]][term[1]])
        else:
            values.append(compute(*term))

    result = sum(map(int,values))
    spreadsheet[i][j] = str(result)
    return spreadsheet[i][j]

def solve(r,c):
    for i in range(r):
        for j in range(c):
            if not _is_calculated(i,j):
                compute(i,j)

def main():
    global spreadsheet
    n = int(input())
    for _ in range(n):
        lines = input().split()
        while len(lines) == 0:
            lines = input().split()
        c,r = list(map(int, lines))
        spreadsheet = [[None for _ in range(c)] for __ in range(r)]
        
        i = 0
        j = 0
        count = 0
        limit = r*c
        for line in sys.stdin:
            data = line.strip().split()
            count += len(data)
            for d in data:
                if j >= c:
                    i += 1
                    j = 0

                spreadsheet[i][j] = d
                j += 1
            
            if count == limit:
                break
              
        solve(r,c)

        for i in range(r):
            for j in range(c):
                if j != 0:
                    print(" ", end="")
                print(spreadsheet[i][j], end="")
            print()

if __name__ == "__main__":
    main()