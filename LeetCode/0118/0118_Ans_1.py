from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        ans = [[1]]
        last_line = [1]
        for _ in range(numRows - 1):
            now_line = [1]
            for j in range(len(last_line) - 1):
                now_line.append(last_line[j] + last_line[j + 1])
            now_line.append(1)
            last_line = now_line
            ans.append(now_line)
        return ans


if __name__ == "__main__":
    print(Solution().generate(5))
