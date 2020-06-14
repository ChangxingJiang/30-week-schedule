class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            hashset = set()
            for j in range(len(s[i:])):
                if s[i:][j] in hashset:
                    if j > ans:
                        ans = j
                    break
                hashset.add(s[i:][j])
            else:
                sub_ans = len(s) - i
                if sub_ans > ans:
                    return sub_ans
                else:
                    return ans
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
    print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
    print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
    print(Solution().lengthOfLongestSubstring(" "))  # 1
    print(Solution().lengthOfLongestSubstring(""))  # 0
    print(Solution().lengthOfLongestSubstring("au"))  # 2
    print(Solution().lengthOfLongestSubstring("ohomm"))  # 3
