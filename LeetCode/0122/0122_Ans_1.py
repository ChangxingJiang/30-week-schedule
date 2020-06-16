from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                sum += profit
        return sum


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
