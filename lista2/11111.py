#Generalized Matrioshkas

SUCCESS_STRING = ":-) Matrioshka!"
FAILURE_STRING = ":-( Try again."

def evaluate(matrioshka):
    if len(matrioshka) % 2 != 0:
        return False
        
    nesting_level_stack = []
    container_size_stack = []

    for number in matrioshka:
        if number < 0:
            nesting_level_stack.append(number)
            container_size_stack.append(0)
        else:
            last_opened_matri = nesting_level_stack.pop()
            #desbalanceada
            if last_opened_matri + number != 0:
                return False
            else:
                container_size_stack.pop()
                if len(container_size_stack) == 0:
                    return True
                container_size_stack[-1] += number
                #tamanho excedeu da ultima matrioshka
                if container_size_stack[-1] >= abs(nesting_level_stack[-1]):
                    return False
    

    return True
    
def main():
    try:
        while True:
            input_string = input()
            numbers = filter(lambda x: x != "", input_string.split(" "))
            matrioshka_candidate = [int(x) for x in numbers]
            result = evaluate(matrioshka_candidate)
            if result:
                print(SUCCESS_STRING)
            else:
                print(FAILURE_STRING)
    except EOFError:
        pass

if __name__ == "__main__":
    main()