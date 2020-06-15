from LeetCode.toolkit import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = node = ListNode(0)

        while l1 or l2:
            if not l1:
                node.next = l2
                break
            if not l2:
                node.next = l1
                break

            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next

            node = node.next

        return ans.next


if __name__ == "__main__":
    print(Solution().mergeTwoLists(ListNode([1, 2, 4]), ListNode([1, 3, 4])))
