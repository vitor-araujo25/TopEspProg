#Slums (?)
import math

def main():
    try:
        while True:
            case = input().strip().split()
            n,p = [int(x) for x in case]
            log_numerator = sum([math.log(i,10) for i in range(n,p,-1)])
            log_denominator = sum([math.log(i,10) for i in range(n-p,0,-1)])
            digits = math.floor(log_numerator - log_denominator) + 1
            print(digits)
    except EOFError:
        return 

if __name__ == "__main__":
    main()