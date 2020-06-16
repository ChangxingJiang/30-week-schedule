from LeetCode.toolkit import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = node = ListNode(0)
        while head:
            if head.next:
                if head.val != head.next.val:
                    node.next = ListNode(head.val)
                    node = node.next
            else:
                node.next = ListNode(head.val)
                node = node.next
            head = head.next
        return ans.next


if __name__ == "__main__":
    print(Solution().deleteDuplicates(ListNode([1, 1, 2])))  # [1,2]
    print(Solution().deleteDuplicates(ListNode([1, 1, 2, 3, 3])))  # [1,2,3]
