from LeetCode.toolkit import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


if __name__ == "__main__":
    print(Solution().deleteDuplicates(ListNode([1, 1, 2])))  # [1,2]
    print(Solution().deleteDuplicates(ListNode([1, 1, 2, 3, 3])))  # [1,2,3]
    print(Solution().deleteDuplicates(ListNode([1, 1, 1, 1, 2, 3, 3])))  # [1,2,3]
