#Tree Summing

from typing import Generator, Tuple


SUCCESS_STRING = "yes"
FAILURE_STRING = "no"

def evaluate(sum, tree):
    pass

def parse(full_input: str): # -> Generator[Tuple[int, str]]:
    full_input = full_input.strip().split(" ")
    full_input = [c for c in full_input if c != ""]
    full_input = "".join(full_input)
    print(full_input)
    # for c in full_input:
    #     if c != 





def main():
    full_input = ""
    try:
        while True:
            input_string = input()
            full_input += input_string            
    except EOFError:
        pass

    parsed_cases = parse(full_input)
    # for goal, tree in parsed_cases:
    #     result = evaluate(goal, tree)
    #     if result:
    #         print(SUCCESS_STRING)
    #     else:
    #         print(FAILURE_STRING)

if __name__ == "__main__":
    main()