class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        now = 5
        while now <= n:
            count += n // now
            now *= 5
        return count


if __name__ == "__main__":
    print(Solution().trailingZeroes(3))  # 0
    print(Solution().trailingZeroes(5))  # 1
    print(Solution().trailingZeroes(1808548329))
