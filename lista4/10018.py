#Reverse and Add

def is_palindrome(value):
    return value[::-1] == value

def main():
    cases = int(input())
    for _ in range(cases):
        iters = 0
        value = input()
        while not is_palindrome(value):
            reverse_val = value[::-1]
            value = str(int(value) + int(reverse_val))
            iters += 1
        print(iters, value)

if __name__ == "__main__":
    main()