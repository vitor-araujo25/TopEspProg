import math
INF = math.inf

def kadane(array):
    max_so_far = -INF
    max_ending_here  = 0

    for i in range(len(array)):
        max_ending_here += array[i]

        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        
    
    return max_so_far

def main():
    while True:
        try:
            n = int(input())
        except:
            continue
        if n == 0:
            break
        i = 0
        bets = []
        while i < n:
            numbers = [int(x) for x in input().strip().split() if x != ""]
            i += len(numbers)
            bets.extend(numbers)

        result = kadane(bets)    

        if result <= 0:
            print("Losing streak.")
        else:
            print(f"The maximum winning streak is {result}.")

if __name__ == "__main__":
    main()