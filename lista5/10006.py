carmichael = {
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973
}

def main():
    while True:
        n = int(input())
        if n == 0: break
        if n in carmichael:
            print(f"The number {n} is a Carmichael number.")
        else:    
            print(f"{n} is normal.")

if __name__ == "__main__":
    main()