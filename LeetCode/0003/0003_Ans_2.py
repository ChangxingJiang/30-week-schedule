class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}  # 距离当前位置最近的字符坐标
        max_long = 0  # 最大长度
        now_long = 0  # 当前位置长度
        for i, c in enumerate(s):
            now_long += 1
            if c in hashmap and i - hashmap[c] < now_long:
                now_long = i - hashmap[c]
            hashmap[c] = i
            if now_long > max_long:
                max_long = now_long
        return max_long


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
    print(Solution().lengthOfLongestSubstring(" "))  # 1
    print(Solution().lengthOfLongestSubstring(""))  # 0
    print(Solution().lengthOfLongestSubstring("au"))  # 2
    print(Solution().lengthOfLongestSubstring("ohomm"))  # 3
    print(Solution().lengthOfLongestSubstring("abba"))  # 2
