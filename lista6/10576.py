from sys import stdin

def solve(s,d):
    months = [s]*12
    j = 0
    i = 5
    while (sum(months[i-5:i])) > 0:
        months[i-j-1] = d
        j += 1
    months[5:10] = months[0:5]
    months[10:] = months[0:2]
    return sum(months)

def main(): 
    for line in stdin:
        s,d = [int(x) for x in line.strip().split() if x != ""]
        result = solve(s,-d)
        if result < 0:
            print("Deficit")
        else:
            print(result)
        

if __name__ == "__main__":
    main()