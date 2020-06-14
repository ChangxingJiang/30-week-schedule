# LeetCode题解：0004（寻找两个正序数组的中位数）

[题目链接](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)（困难）

| 解法           | 时间复杂度         | 空间复杂度 | 执行用时       | 内存消耗        |
| -------------- | ------------------ | ---------- | -------------- | --------------- |
| Ans 1 (Python) | $O((M+N)log(M+N))$ | $O(M+N)$   | 40ms (>98.73%) | 13.7MB (>6.15%) |
| Ans 2 (Python) | $O(M+N)$           | $O(1)$     | 48ms (>89.95%) | 13.7MB (>6.15%) |
| Ans 3 (Python) | $O(log(M+N))$      | $O(1)$     | 80ms (>11.71%) | 13.8MB (>6.15%) |

解法一（直接合并数组排序求中位数）：

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    count = len(nums)
    if count % 2 == 0:
        return (nums[int(count / 2 - 1)] + nums[int(count / 2)]) / 2
    else:
        return nums[int(count / 2)]
```

解法二（直接寻找中位数的位置）：

```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    len_1 = len(nums1)
    len_2 = len(nums2)
    total = len_1 + len_2

    left = -1
    right = -1

    index_1 = 0
    index_2 = 0

    for i in range(int(total / 2) + 1):
        left = right
        if index_1 < len_1 and (index_2 >= len_2 or nums1[index_1] < nums2[index_2]):
            right = nums1[index_1]
            index_1 += 1
        else:
            right = nums2[index_2]
            index_2 += 1

    if total % 2 == 0:
        return (left + right) / 2
    else:
        return right
```

解法三（使用二分查找寻找中位数的位置）：

```python
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
```

