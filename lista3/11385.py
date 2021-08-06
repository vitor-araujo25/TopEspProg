#Da Vinci Code
from functools import lru_cache

@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)

FIBONACCI_MAP = {fib(i): i for i in range(1,45)}

def solve(N, fib_numbers, cipher):
    message = [' ']*100

    fib_index = 0
    for c in cipher:
        if ord(c) < ord('A') or ord(c) > ord('Z'):
            continue
        if fib_index == N:
            break
        key = fib_numbers[fib_index]
        true_position = FIBONACCI_MAP[key] - 1
        message[true_position] = c
        fib_index += 1

    return "".join(message).rstrip()

def main():
    cases = int(input())
    for _ in range(cases):
        input_len = int(input())
        fibs = [int(x) for x in input().strip().split(" ")]
        cipher = input().strip()
        print(solve(input_len, fibs, cipher))

if __name__ == "__main__":
    main()