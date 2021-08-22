#Big Big Real Numbers

def build_number(integer_part, decimal_part):
    while len(integer_part) != 1 and integer_part[0] == "0":
        integer_part = integer_part[1:]
    while len(decimal_part) != 1 and decimal_part[-1] == "0":
        decimal_part = decimal_part[:-1]

    return ".".join([integer_part, decimal_part])

def trim_and_split_number(number):
    parts =  [x for x in number.split(".")]

    if len(parts) == 1:
        parts[0] = parts[0].lstrip("0")
        parts.append("0")
        part_int, part_dec = parts
    else:
        part_int, part_dec = parts
        if len(part_int) > 1:
            part_int = part_int.lstrip("0")
        if len(part_dec) > 1:
            part_dec = part_dec.rstrip("0")

    if part_int == "": part_int = "0"
    if part_dec == "": part_dec = "0"
    return part_int, part_dec

#a: list[str]:: [int_part, dec_part]
#b: list[str]:: [int_part, dec_part]
def _sum_same_signal_aligned(a,b):
    
    a_int, a_dec = a
    b_int, b_dec = b
    
    carry = 0   
    sum_dec = ""

    for i in range(len(a_dec)-1,-1,-1):
        piece_sum = (int(a_dec[i]) + int(b_dec[i]) + carry)
        carry = piece_sum // 10     
        value = piece_sum % 10
        sum_dec = str(value) + sum_dec
    
    sum_int = ""

    for i in range(-1, -(len(a_int)+1), -1):
        piece_sum = (int(a_int[i]) + int(b_int[i]) + carry)
        carry = piece_sum // 10
        value = piece_sum % 10
        sum_int = str(value) + sum_int  

    return carry, sum_int, sum_dec
    
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
    one =  ["0"*len(number_int), ("0"*(len(number_dec)-1))+"1"]
    carry, int_result, dec_result = _sum_same_signal_aligned([number_int, number_dec], one)

    if carry == 1:
        int_result = "1" + int_result
    
    return int_result, dec_result

    
def solve_sum(a,b):
    a_int, a_dec = trim_and_split_number(a)
    b_int, b_dec = trim_and_split_number(b)

    #align around decimal point
    a_int = a_int.rjust(len(b_int),"0")
    b_int = b_int.rjust(len(a_int),"0")
    a_dec = a_dec.ljust(len(b_dec),"0")
    b_dec = b_dec.ljust(len(a_dec),"0")

    a = [a_int, a_dec]
    b = [b_int, b_dec]

    carry, int_part, dec_part = _sum_same_signal_aligned(a,b)

    if carry == 1:
        int_part = "1" + int_part

    return build_number(int_part, dec_part)


def solve_subtraction(a,b):
    pos, neg = (b,a) if a[0] == "-" else (a,b)

    pos_int, pos_dec = trim_and_split_number(pos)
    
    #removing negative sign
    neg_int, neg_dec = trim_and_split_number(neg[1:])
  
    #align around decimal point
    neg_int = neg_int.rjust(len(pos_int),"0")
    pos_int = pos_int.rjust(len(neg_int),"0")
    neg_dec = neg_dec.ljust(len(pos_dec),"0")
    pos_dec = pos_dec.ljust(len(neg_dec),"0")

    pos = [pos_int, pos_dec]
    neg = tens_complement(neg_int, neg_dec)

    carry, int_part, dec_part = _sum_same_signal_aligned(pos, neg)

    if carry == 0:
        return "-"+build_number(*tens_complement(int_part, dec_part))
    else:
        return build_number(int_part,dec_part)


def main():
    cases = int(input())
    for i in range(cases):
        a,b = [x for x in input().strip().split() if x != ""]
        if a[0] != "-" and b[0] != "-" :
            print(solve_sum(a,b))
        elif a[0] == "-" and b[0] == "-" : 
            solution = solve_sum(a[1:],b[1:])
            if solution == "0.0":
                print(solution)
            else:
                print("-"+solution)
        else:
            print(solve_subtraction(a,b))

if __name__ == "__main__":
    main()