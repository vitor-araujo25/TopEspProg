#Stacks of Flapjacks

#@steps: (flip_pos, size_stack)
def solve(stack, steps):
    if len(stack) == 1:
        steps.append((0, len(stack)))
        return
    largest_pancake = (stack[-1], -1) #size, position
    for i in range(1,len(stack)+1):
        pancake = stack[-i]
        if pancake > largest_pancake[0]:
            largest_pancake = (pancake, -i)

    if largest_pancake[1] == -1: #maior no lugar certo, nada a fazer
        solve(stack[:-1], steps)
    elif largest_pancake[1] == -len(stack): #maior no topo, virar a pilha toda
        steps.append((1, len(stack)))
        solve(stack[::-1], steps)
    else:
        steps.append((-largest_pancake[1], len(stack)))  #maior no meio, viro as de cima e mantem a pilha abaixo
        solve(stack[largest_pancake[1]:-(len(stack)+1):-1] + stack[largest_pancake[1]+1:], steps)
        
    return

def main():
    while True:
        try:
            stack = input().strip().split(" ")
            print(" ".join(stack))
            steps = []
            solve([int(p) for p in stack], steps)
            # print(steps)
            print(" ".join([str(step[0] + (len(stack)-step[1])) if step[0] != 0 else str(0) for step in steps]))
        except EOFError:
            break

if __name__ == "__main__":
    main()