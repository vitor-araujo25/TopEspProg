#Find the ways!
import math
from sys import stdin
import time


def _get_chunk(n):
    if n > 1e8:
        chunk_size = 1e7
    elif n > 1e6:
        chunk_size = 1e5
    elif n > 1e4:
        chunk_size = 1e3
    elif n > 1e2:
        chunk_size = 1e1
    else:
        chunk_size = 1

    chunk_size = int(chunk_size)

    return chunk_size

def partition_log(n,p):
    chunk_size =_get_chunk(n)
    rem = n % chunk_size
    print(list(range(n, n-rem, -1)))
    print(list(range(n-rem, p+chunk_size, -chunk_size)))
    print(list(range(p+chunk_size, p, -1)))
    
    chunk_size = _get_chunk(n-p)
    rem = (n-p) % chunk_size
    print(list(range(n-p, n-p-rem, -1)))
    print(list(range(n-p-rem, chunk_size-1, -chunk_size)))
    print(list(range(chunk_size-1, 1, -1)))
    


def main():
    for line in stdin:
            case = line.strip().split()
            # start = time.time()
            n,p = [int(x) for x in case]
            partition_log(n,p)
            log_numerator = sum([math.log(i,10) for i in range(n,p,-1)])
            log_denominator = sum([math.log(i,10) for i in range(n-p,0,-1)])
            digits = math.floor(log_numerator - log_denominator) + 1
            print(digits)
            # print(f"t: {time.time()-start}")

if __name__ == "__main__":
    main()