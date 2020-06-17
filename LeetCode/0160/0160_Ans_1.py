from LeetCode.toolkit import ListNode, build_ListNode_with_skip


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashmap = set()
        while headA:
            hashmap.add(headA)
            headA = headA.next
        while headB:
            if headB in hashmap:
                return headB
            headB = headB.next


if __name__ == "__main__":
    list1, list2 = build_ListNode_with_skip(8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3)
    print(list1, list2)
    print(Solution().getIntersectionNode(list1, list2))
    list1, list2 = build_ListNode_with_skip(2, [0, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    print(Solution().getIntersectionNode(list1, list2))
    list1, list2 = build_ListNode_with_skip(0, [2, 6, 4], [1, 5], 3, 2)
    print(Solution().getIntersectionNode(list1, list2))
