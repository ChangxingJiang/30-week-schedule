from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset = set()
        del_list = []
        for i in range(len(nums)):
            d = nums[i]
            if d not in hashset:
                hashset.add(d)
            else:
                del_list.append(i)

        for i in del_list[::-1]:
            nums.pop(i)

        return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums), nums)  # [1,2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums), nums)  # [0,1,2,3,4]
    nums = [-1, 0, 0, 0, 0, 3, 3]
    print(Solution().removeDuplicates(nums), nums)  # [-1,0,3]
