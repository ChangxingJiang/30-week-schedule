from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            row = [1, 1]
            for _ in range(1, rowIndex):
                new_row = [1]
                for i in range(len(row) - 1):
                    new_row.append(row[i] + row[i + 1])
                new_row.append(1)
                row = new_row
            return row


if __name__ == "__main__":
    print(Solution().getRow(3))  # [1,3,3,1]
