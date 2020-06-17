class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            ans.append(chr((n - 1) % 26 + 65))
            n = (n - 1) // 26
        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().convertToTitle(1))  # A
    print(Solution().convertToTitle(28))  # AB
    print(Solution().convertToTitle(701))  # ZY
    print(Solution().convertToTitle(26))  # Z
