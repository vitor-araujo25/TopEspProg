import collections 

def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return factors

def main():
    while True:
        try:
            factorial, divisor = [int(x) for x in input().split()]
            divisor_factors = collections.Counter(prime_factors(divisor))
            # print(divisor_factors.items())

            divides = True
            for prime, multiplicity in divisor_factors.items():
                t_freq = 0
                aux = prime
                while factorial >= aux:
                    t_freq += factorial // aux
                    aux *= prime
                if t_freq < multiplicity:
                    divides = False
                    break

            if not divides:
                print(f"{divisor} does not divide {factorial}!")
            else:
                print(f"{divisor} divides {factorial}!")
        except EOFError:
            break

if __name__ == "__main__":
    main()



