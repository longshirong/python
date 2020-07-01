from typing import List

"""
322. 零钱兑换
https://leetcode-cn.com/problems/coin-change/
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

"""


def coinChange(coins: List[int], amount: int) -> int:
    if not coins:
        return -1
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin])
    if dp[-1] == amount+1:
        return -1
    else:
        return dp[-1]


class Solution:
    pass

