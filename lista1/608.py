diffs = [-1, 1]
balances = {
    "up": -1,
    "down": 1,
    "even": 0
}
weights = {
    -1: "light",
    1: "heavy"
}

def check(measure, coin_id, diff):
    left, right = 0, 0
    if coin_id in measure["left"]:
        left = diff
    if coin_id in measure["right"]:
        right = diff
    return right - left == measure["balance"]

def try_coin(coin_id, measures):
    for diff in diffs:
        for measure in measures:
            if not check(measure, coin_id, diff):
                break
        else:
            return coin_id, diff

def evaluate(measures):
    for coin_id in "ABCDEFGHIJKL":
        result = try_coin(coin_id, measures)
        if result is not None:
            return result

count = int(input())

for i in range(count):
    measures = []
    for j in range(3):
        line = input()
        left,right,balance = line.strip().split(" ")
        measures.append({
            "left": left,
            "right": right,
            "balance": balances[balance]
        })
    counterfeit, diff = evaluate(measures)
    print("{} is the counterfeit coin and it is {}.".format(counterfeit, weights[diff]))
