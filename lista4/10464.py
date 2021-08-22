#Big Big Real Numbers

def build_number(integer_part, decimal_part):
    print(f"joining {integer_part} and {decimal_part}")
    while len(integer_part) != 1 and integer_part[0] == "0":
        integer_part = integer_part[1:]
    while len(decimal_part) != 1 and decimal_part[-1] == "0":
        decimal_part = decimal_part[:-1]

    return ".".join([integer_part, decimal_part])

def break_number(number):
    parts =  [x if x != "" else "0" for x in number.split(".")]
    if len(parts) == 1:
        parts.append("0")
    a_int, a_dec = parts
    if a_int == "-": a_int = "-0"
    return a_int, a_dec

#a: list[str]:: [int_part, dec_part]
#b: list[str]:: [int_part, dec_part]
def _positive_sum(a,b):
    
    a_int, a_dec = a
    b_int, b_dec = b

    print(f"summing: {a_int}.{a_dec} + {b_int}.{b_dec}")

    carry = 0
    longest, shortest = (a_dec, b_dec) if len(a_dec) > len(b_dec) else (b_dec, a_dec)
    shortest = shortest.ljust(len(longest),"0")
    sum_dec = longest[len(shortest):]

    for i in range(len(shortest)-1,-1,-1):
        piece_sum = (int(shortest[i]) + int(longest[i]) + carry)
        carry = piece_sum // 10     
        value = piece_sum % 10
        sum_dec = str(value) + sum_dec

    longest, shortest = (a_int, b_int) if len(a_int) > len(b_int) else (b_int, a_int)
    shortest = shortest.rjust(len(longest),"0")
    sum_int = ""

    for i in range(-1, -(len(shortest)+1), -1):
        piece_sum = (int(shortest[i]) + int(longest[i]) + carry)
        carry = piece_sum // 10
        value = piece_sum % 10
        sum_int = str(value) + sum_int  
        
    for j in range(i-1, -(len(longest)+1), -1):
        piece_sum = (int(longest[j]) + carry)
        carry = piece_sum // 10
        value = piece_sum % 10
        sum_int = str(value) + sum_int

    return carry, sum_int, sum_dec
    

def solve_positive_sum(a,b):
    a = break_number(a)
    b = break_number(b)
    carry, int_part, dec_part = _positive_sum(a,b)

    if carry == 1:
        int_part = "1" + int_part

    return build_number(int_part, dec_part)



def tens_complement(number_int, number_dec):
    result = ""

    for i in range(len(number_dec)):
        new_element = 9 - int(number_dec[i])
        result += str(new_element)

    number_dec = result
    result = ""

    for i in range(len(number_int)):
        new_element = 9 - int(number_int[i])
        result += str(new_element)

    number_int = result
    one =  ["0", ("0"*(len(number_dec)-1))+"1"]
    # print(f"number: {number_int}.{number_dec} one: {one}")
    carry, int_result, dec_result = _positive_sum([number_int, number_dec], one)

    if carry == 1:
        int_result = "1" + int_result
    
    return int_result, dec_result


def solve_subtraction(a,b):
    pos, neg = (b,a) if a[0] == "-" else (a,b)

    pos = break_number(pos)
    neg = break_number(neg)
    print(f"normal: {neg}")
    neg = tens_complement(neg[0][1:], neg[1])
    print(f"tens: {neg}")

    carry, int_part, dec_part = _positive_sum(pos, neg)
    print(f"tens complement sum: {int_part}.{dec_part}, with carry {carry}")  
    if carry == 0:
        return "-"+build_number(*tens_complement(int_part, dec_part))
    else:
        return build_number(int_part,dec_part)


def main():
    cases = int(input())
    for i in range(cases):
        a,b = [x for x in input().strip().split() if x != ""]
        a = a.strip("0")
        b = b.strip("0")
        if a[0] != "-" and b[0] != "-" :
            print(solve_positive_sum(a,b))
        elif a[0] == "-" and b[0] == "-" : 
            solution = solve_positive_sum(a[1:],b[1:])
            if solution == "0.0":
                print(solution)
            else:
                print("-"+solution)
        else:
            print(solve_subtraction(a,b))

if __name__ == "__main__":
    main()