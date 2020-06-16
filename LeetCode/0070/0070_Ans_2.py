class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {1: 1, 2: 2}
        if n < 3:
            return hashmap[n]
        for i in range(3, n + 1):
            hashmap[i] = hashmap[i - 1] + hashmap[i - 2]
        return hashmap[n]


if __name__ == "__main__":
    print(Solution().climbStairs(2))  # 2
    print(Solution().climbStairs(3))  # 3
    print(Solution().climbStairs(10))  # 89
    print(Solution().climbStairs(20))  # 89
