#Counterfeit Dollar
translate = {
    "up": 1,
    "even": 0,
    "down": -1
}

count = int(input())

for i in range(count):
    
    mapping = {letter: None for letter in "ABCDEFGHIJKL"}

    for j in range(3):
        line = input()
        left,right,balance = line.split(" ")
        
        if balance == "even":
            for l in left:
                mapping[l] = 0
            for l in right:
                mapping[l] = 0
        if balance == "up":
            for l in left:
                if mapping[l] is None: 
                    mapping[l] = -1
                    continue
                if mapping[l] == 0: continue
                mapping[l] -= 1
            for l in right:
                if mapping[l] is None: 
                    mapping[l] = 1
                    continue
                if mapping[l] == 0: continue
                mapping[l] += 1
        if balance == "down":
            for l in left:
                if mapping[l] is None: 
                    mapping[l] = 1
                    continue
                if mapping[l] == 0: continue
                mapping[l] += 1
            for l in right:
                if mapping[l] is None: 
                    mapping[l] = -1
                    continue
                if mapping[l] == 0: continue
                mapping[l] -= 1

    print(mapping)