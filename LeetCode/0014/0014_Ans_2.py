from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for s in zip(*strs):
            if len(set(s)) != 1:
                return ans
            else:
                ans += s[0]
        return ans


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix([]))
    print(Solution().longestCommonPrefix([""]))
    print(Solution().longestCommonPrefix(["a"]))
