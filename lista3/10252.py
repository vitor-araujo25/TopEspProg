def solve(a, b):
    if a == "" or b == "":
        return ""
    a_count = [0 for _ in range(26)]
    b_count = [0 for _ in range(26)]
    common = [0 for _ in range(26)]

    for letter in a:
        a_count[ord(letter) - ord('a')] += 1
    for letter in b:
        b_count[ord(letter) - ord('a')] += 1

    for i in range(26):
        common[i] = min(a_count[i], b_count[i])

    return "".join([chr(i + ord('a'))*common[i] for i in range(len(common))])


def main():
    while True:
        try:
            first = input()
            second = input()
            print(solve(first, second))
        except EOFError:
            break

if __name__ == "__main__":
    main()