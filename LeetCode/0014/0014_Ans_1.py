from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 处理空列表的情况
        if len(strs) == 0:
            return ""

        # 统计最长的字符串长度
        min_len = min([len(s) for s in strs])

        # 处理只有空字符串的情况
        if min_len == 0:
            return ""

        for i in range(min_len):
            t = strs[0][i]
            for s in strs:
                if s[i] != t:
                    return strs[0][0:i]
        return strs[0][0:min_len]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix([]))
    print(Solution().longestCommonPrefix([""]))
    print(Solution().longestCommonPrefix(["a"]))
