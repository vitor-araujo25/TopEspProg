#Password Search
from sys import stdin
from collections import defaultdict

def solve(n: int, text: str):
    counter = defaultdict(lambda: 0)
    for i in range(len(text)-n+1):
        counter[text[i:i+n]] += 1
    most_frequent = ('',0)
    for password,occurrences in counter.items():
        if occurrences > most_frequent[1]:
            most_frequent = (password, occurrences)

    return most_frequent[0]

def main():
    while True:
        try:

            line = input()
            if line == "":
                continue
            line = line.strip().split(" ")
            if len(line) == 2:
                n = line[0]
                text = line[1]
            else:
                n = line[0]
                text = input().strip()
                while text == "":
                    text = input().strip()

            print(solve(int(n), text))
        except EOFError:
            return

if __name__ == "__main__":
    main()