from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        now = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            now += profit
            if now < profit:
                now = profit
            if now > maximum:
                maximum = now
        return maximum


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
    print(Solution().maxProfit([1]))  # 0
    print(Solution().maxProfit([]))  # 0
