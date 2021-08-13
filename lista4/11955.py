#Binomial Theorem
import re
from functools import lru_cache

PATTERN = re.compile("\((\w+)\+(\w+)\)\^(\d+)")

@lru_cache
def fat(n):
    if n == 0: return 1
    return n * fat(n-1)

def comb(n,p):
    return fat(n)//(fat(p)*fat(n-p))

def build_term(base, exponent):
    if exponent > 1:
        return base + '^' + str(exponent)
    elif exponent == 1:
        return base
    else:
        return ""

def solve(a,b,k):
    # print(a,b,k)
    terms = []
    k = int(k)
    for i in range(k, -1, -1):
        term = ""
        scalar = comb(k, i)
        if scalar > 1:
            term += str(scalar)+'*'
        a_exponent = i
        b_exponent = k-i
        term_a = build_term(a, a_exponent)
        term_b = build_term(b, b_exponent)
        partial_term = '*'.join([term for term in [term_a, term_b] if term != ""])
        # print(term, partial_term)
        term += partial_term if partial_term != '*' else ''
        terms.append(term)
    return terms
        

def main():
    cases = int(input())
    for i in range(1,cases+1):
        case = PATTERN.findall(input().strip())
        # print(case)
        print(f"Case {i}: {'+'.join(solve(*case[0]))}")

if __name__ == "__main__":
    main()