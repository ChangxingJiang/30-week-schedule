class Solution:
    def isValid(self, s: str) -> bool:

        sign_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        sign_list = []
        for c in s:
            if c in ["(", "[", "{"]:
                sign_list.append(c)
            else:
                r = sign_dict[c]
                if sign_list and r == sign_list[-1]:
                    sign_list.pop()
                else:
                    return False

        if sign_list:
            return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isValid("()"))  # True
    print(Solution().isValid("()[]{}"))  # True
    print(Solution().isValid("(]"))  # False
    print(Solution().isValid("([)]"))  # False
    print(Solution().isValid("{[]}"))  # True
    print(Solution().isValid("["))  # False
    print(Solution().isValid("]"))  # False
    print(Solution().isValid("(([]){})"))  # True
    print(Solution().isValid("[([]])"))  # False
