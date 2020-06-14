from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2)
        total = len_1 + len_2

        if len_1 == 0:
            if total % 2 == 0:
                return (nums2[int(total / 2 - 1)] + nums2[int(total / 2)]) / 2
            else:
                return nums2[int(total / 2)]

        if len_2 == 0:
            if total % 2 == 0:
                return (nums1[int(total / 2 - 1)] + nums1[int(total / 2)]) / 2
            else:
                return nums1[int(total / 2)]

        middle_num = (total + 1) // 2

        index_1 = -1
        index_2 = -1

        already_num = 0
        while True:
            surplus_num = middle_num - already_num  # 剩余总量
            if surplus_num == 1:
                find_number = 1  # 这一次二分的数量
            else:
                find_number = surplus_num // 2  # 这一次二分的数量

            binery_index_1 = index_1 + find_number
            binery_index_2 = index_2 + find_number
            # print(binery_index_1, binery_index_2)
            if binery_index_1 >= len_1:
                binery_index_1 = len_1 - 1
            if binery_index_2 >= len_2:
                binery_index_2 = len_2 - 1

            if index_1 == len_1 - 1:
                already_num += binery_index_2 - index_2
                index_2 = binery_index_2
            if index_2 == len_2 - 1:
                already_num += binery_index_1 - index_1
                index_1 = binery_index_1

            # print(binery_index_1, binery_index_2)
            if nums1[binery_index_1] < nums2[binery_index_2]:
                already_num += binery_index_1 - index_1
                index_1 = binery_index_1
            else:
                already_num += binery_index_2 - index_2
                index_2 = binery_index_2
            print("List1[" + str(binery_index_1) + "] =", nums1[binery_index_1], ",",
                  "List2[" + str(binery_index_2) + "] =", nums2[binery_index_2],
                  "→", min(nums1[binery_index_1], nums2[binery_index_2]), "(", already_num, ")", "-",
                  index_1, index_2)
            if already_num >= middle_num:
                break

        print("index_1 =", index_1, "; index_2 =", index_2)

        if index_1 == -1:
            now_number = nums2[index_2]
            # print("Now:", index_2, nums2[index_2])
        elif index_2 == -1:
            now_number = nums1[index_1]
            # print("Now:", index_1, nums1[index_1])
        else:
            now_number = max(nums1[index_1], nums2[index_2])
            # print("Now:", index_1, nums1[index_1], ",", index_2, nums2[index_2])

        if index_1 + 1 >= len_1:
            next_number = nums2[index_2 + 1]
        elif index_2 + 1 >= len_2:
            next_number = nums1[index_1 + 1]
        else:
            next_number = min(nums1[index_1 + 1], nums2[index_2 + 1])

        print("Now:", now_number, ";Next:", next_number)

        if total % 2 == 1:
            return now_number
        else:
            return (now_number + next_number) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))  # 2
    print(Solution().findMedianSortedArrays([1, 3], [2, 4]))  # 2.5
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
    print(Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8]))  # 5.5
    print(Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))  # 5.5
    print(Solution().findMedianSortedArrays([], [1]))  # 1
    print(Solution().findMedianSortedArrays([1], [2, 3]))  # 2
    print(Solution().findMedianSortedArrays([1], [2, 3, 4, 5]))  # 3
