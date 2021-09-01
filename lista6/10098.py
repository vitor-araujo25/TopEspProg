#Generating Fast
import itertools

def main():
    cases = int(input())
    for _ in range(cases):
        case = input()
        uniques = set()
        for perm in itertools.permutations(sorted(case)):
            word = "".join(perm)
            if word not in uniques:
                uniques.add(word)
                print(word)
        print()

if __name__ == "__main__":
    main()