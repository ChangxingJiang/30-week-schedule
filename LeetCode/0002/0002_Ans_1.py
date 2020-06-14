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
        ans = ListNode(0)  # 返回结果
        carry = 0  # 进位计数
        node = ans  # 当前位
        while True:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            node.val = value % 10
            carry = value // 10
            if l1 or l2 or carry == 1:
                node.next = ListNode(0)
                node = node.next
            else:
                break
        return ans


if __name__ == "__main__":
    print(Solution().addTwoNumbers(l1=ListNode([2, 4, 3]), l2=ListNode([5, 6, 4])))
    print(Solution().addTwoNumbers(l1=ListNode([5]), l2=ListNode([5])))
