from typing import List
"""
322. 零钱兑换
https://leetcode-cn.com/problems/coin-change/
输入: coins = [1, 2, 5], amount = 11
输出: 3 
"""


def coinChange(coins: List[int], amount: int) -> int:
    if not coins:
        return -1
    if amount == 0:
        return 0
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for j in coins:
            if i >= j:
                dp[i] = min(dp[i], dp[i-j] + 1)
    if dp[-1] == amount+1:
        return -1
    else:
        return dp[-1]


class Solution:
    coins = [1, 2, 5]
    amount = 11
    coinChange(coins, amount)

