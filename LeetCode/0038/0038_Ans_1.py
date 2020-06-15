class Solution:
    def countAndSay(self, n: int) -> str:

        def count(s):
            new = ""
            last = None
            num = 0
            for c in s:
                if c != last:
                    if num > 0:
                        new += str(num) + last
                    last = c
                    num = 1
                else:
                    num += 1
            if num > 0:
                new += str(num) + last
            return new

        s = "1"
        for i in range(1, n):
            s = count(s)
        return s


if __name__ == "__main__":
    print("返回值:", Solution().countAndSay(1))  # 1
    print("返回值:", Solution().countAndSay(4))  # 1211
