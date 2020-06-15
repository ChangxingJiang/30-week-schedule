class ListNode:
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
        if isinstance(val, int):
            self.val = val
            self.next = None
        elif isinstance(val, list):
            if len(val) == 1:
                self.val = val[0]
                self.next = None
            else:
                self.val = val[0]
                self.next = ListNode(val[1:])

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class TreeNode:
    """
    LeetCode官方TreeNode类仿写（模拟官方功能）
    主要用于本地IDE调试
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


if __name__ == "__main__":
    print(ListNode([1, 3, 5]))  # ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    print(tree)
    # TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
