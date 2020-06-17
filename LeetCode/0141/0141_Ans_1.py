from LeetCode.toolkit import ListNode, build_ListNode_with_pos


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashset = set()
        while head:
            if head in hashset:
                return True
            else:
                hashset.add(head)
                head = head.next
        return False


if __name__ == "__main__":
    print(Solution().hasCycle(build_ListNode_with_pos([3, 2, 0, -4], pos=1)))  # True
    print(Solution().hasCycle(build_ListNode_with_pos([1, 2], pos=0)))  # True
    print(Solution().hasCycle(build_ListNode_with_pos([1], pos=-1)))  # False
