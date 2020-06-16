class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(t) for t in a]
        b = [int(t) for t in b]

        len_a = len(a)
        len_b = len(b)

        s = []
        add = 0
        for i in range(1, max(len_a, len_b) + 1):
            c = add
            if i <= len_a:
                c += a[-i]
            if i <= len_b:
                c += b[-i]
            if c == 0:
                s.insert(0, "0")
                add = 0
            elif c == 1:
                s.insert(0, "1")
                add = 0
            elif c == 2:
                s.insert(0, "0")
                add = 1
            else:
                s.insert(0, "1")
                add = 1
        if add == 1:
            s.insert(0, "1")
        return "".join(s)


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))  # 100
    print(Solution().addBinary("1010", "1011"))  # 10101
