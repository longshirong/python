from typing import List
"""
518. 零钱兑换 II
https://leetcode-cn.com/problems/coin-change-2/
输入: amount = 5, coins = [1, 2, 5]
输出: 4
"""


def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount+1)
    dp[0] = 1
    for j in coins:
        for i in range(1, amount+1):
            if i >= j:
                dp[i] = dp[i] + dp[i-j]
    return dp[-1]


class Solution:
    amount = 5
    coins = [1, 2, 5]
    change(amount, coins)