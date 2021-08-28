import math

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        if n == int(math.sqrt(n))**2: #odd divisors
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()