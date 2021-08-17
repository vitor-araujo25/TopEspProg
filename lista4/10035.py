#Primary Arithmetic


def carry(bigger, smaller):
    carry_count=0
    has_carry=0
    for i in range(-1, -(len(smaller)+1), -1):
        has_carry = (int(smaller[i]) + int(bigger[i]) + has_carry) // 10             
        carry_count += has_carry
        
    for j in range(i-1, -(len(bigger)+1), -1):
        has_carry = (int(bigger[j]) + has_carry) // 10 
        carry_count += has_carry
    
    return carry_count

def solve(n1, n2):
    
    if len(n2) > len(n1):
        carry_count = carry(n2, n1)
    else:
        carry_count = carry(n1, n2)

    return carry_count


def main():
    while True:
        case = [i for i in input().strip().split() if i != ""]
        if case[0] == "0" and case[1] == "0":
            break
        carry_count = solve(*case)
        print(f"{carry_count if carry_count > 0 else 'No'} carry operation{'s' if carry_count > 1 else ''}.")

if __name__ == "__main__":
    main()