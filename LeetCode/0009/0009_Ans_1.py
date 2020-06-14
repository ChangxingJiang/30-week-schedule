import copy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = [c for c in str(x)]
        r = copy.deepcopy(l)
        r.reverse()
        return l == r


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
