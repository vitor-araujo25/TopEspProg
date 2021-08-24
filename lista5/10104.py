#Euclid Problem
from sys import stdin

def EuclidianoEstendido(a,b):
    alfa_2 = 1
    beta_2 = 0
    alfa_1 = 0
    beta_1 = 1
    resto = a%b
    quociente = a//b
    if resto == 0:
        return alfa_1,beta_1,b
    else:
        while(resto != 0):
            alfa = alfa_2 - (alfa_1*quociente)
            beta = beta_2 - (beta_1*quociente)
            a,b = b,resto
            resto = a%b
            quociente = a//b
            alfa_2 = alfa_1
            beta_2 = beta_1
            beta_1 = beta
            alfa_1 = alfa
        return alfa,beta,b

for line in stdin:
    a,b = [int(x) for x in line.strip().split() if x != ""]
    alfa,beta,mdc = EuclidianoEstendido(a,b)
    print(f"{alfa} {beta} {mdc}")