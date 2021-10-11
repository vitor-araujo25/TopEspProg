COKE_PRICE = 8


def main():
    cases = int(input())
    for _ in range(cases):
        cokes, n1, n5, n10 = [int(x) for x in input().strip().split() if x != ""]
        wallet = {
            1: n1,
            5: n5,
            10: n10
        }
        total_coins = 0
        # i = 0
        sorted_keys = sorted(wallet.keys(), reverse=True)
        while cokes > 0:
            unpaid = cokes*COKE_PRICE
            cokes_bought = 0
            change = 0
            while unpaid != 0:
                
                pass

            cokes -= cokes_bought

            # change = 0
            # while unpaid != 0:
            #     greed = max(wallet.items(), key=lambda x: x[0] if x[1] != 0 else 0)
            #     div = unpaid / greed[0]
            #     if div < 1:
            #         change = greed[0] - unpaid
            #         wallet[greed[0]] -= 1
            #         unpaid = 0
            #         total_coins += 1
            #     else:
            #         mult = div if round(div) == div else 1
            #         mult = min(mult, greed[1])
            #         unpaid -= greed[0]*mult
            #         total_coins += mult
            #         wallet[greed[0]] -= mult
            # while change != 0:
            #     greed = max(wallet.keys(), key=lambda x: x if x <= change else 0)
            #     change -= greed
            #     wallet[greed] += 1
        print(int(total_coins))
         

if __name__ == "__main__":
    main()