from sys import stdin
import math

def solve(k):
    solutions = []
    for y in range(k+1,2*k+1):
        x = (k*y)/(y-k)
        
        if math.floor(x) == x:
            solutions.append(f"1/{k} = 1/{int(x)} + 1/{int(y)}")

    print(len(solutions))
    if len(solutions) != 0:
        for sol in solutions:
            print(sol)
            
def main():
    for line in stdin:
        k = int(line.strip())
        solve(k)    

if __name__ == "__main__":
    main()