class ListNode():
    """
    LeetCode官方ListNode类仿写（模拟官方功能）
    主要用于本地IDE调试

    参考：https://leetcode-cn.com/problems/add-two-numbers/solution/python3ti-jie-fang-leetcodeguan-fang-lei-listnoded/

    """

    def __init__(self, val):
        """
        构造器
        :param val: 构造对象
        """
        print(val)
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
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


if __name__ == "__main__":
    print(ListNode([1, 3, 5]))  # ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
