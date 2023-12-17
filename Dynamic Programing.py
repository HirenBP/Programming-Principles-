"""
Given a set of coin values coins = {c1, c2,...,ck} and a target sum of money m, what's the minimum
number of coins that form the sum m?
"""

def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

memo = {}
def minimum_coins(m, coins):
    if m in memo:
        return memo[m]
    if m == 0:
        ans = 0
    else:
        ans = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                continue
            ans = min_ignore_none(ans, minimum_coins(subproblem, coins) + 1)
    memo[m] = ans
    return ans

print(minimum_coins(150,[1,4,5]))


