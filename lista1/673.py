#Parentheses Balance
def evaluate(input_string):
    if input_string == "":
        return "Yes"
    stack = []
    for c in input_string:
        try:
            if c == "(" or c == "[":
                stack.append(c)
            elif c == ")":
                top = stack.pop()
                if top != "(": return "No"
            elif c == "]":
                top = stack.pop()
                if top != "[": return "No"
        except IndexError:
            return "No"
    if len(stack) != 0: return "No"
    return "Yes"

count = int(input())

for i in range(count):
    val = input()
    print(evaluate(val))