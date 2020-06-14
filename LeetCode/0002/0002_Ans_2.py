class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = node = ListNode(None)  # 返回结果 当前节点
        now = 0  # 进位计数
        while l1 or l2 or now:
            now += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            node.next = ListNode(now % 10)
            node = node.next
            now //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next


if __name__ == "__main__":
    print(Solution().addTwoNumbers(l1=ListNode([2, 4, 3]), l2=ListNode([5, 6, 4])))
    print(Solution().addTwoNumbers(l1=ListNode([5]), l2=ListNode([5])))
