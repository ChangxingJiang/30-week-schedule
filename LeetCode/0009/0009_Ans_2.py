class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # 处理负数的情况
            return False

        original = x  # 原始数值
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x //= 10

        return original == ans


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
