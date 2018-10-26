# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        dot, e = False, False
        i = 0
        while i < len(s):
            if s[i] == "+" or s[i] == "-":
                if i == 0 or s[i - 1] == "e" or s[i - 1] == "E":
                    pass
                else:
                    return False
            elif s[i] == "e" or s[i]== "E":
                if e:
                    return False
                else:
                    e = True
            elif s[i] == ".":
                if dot or e:
                    return False
                else:
                    dot = True
            elif not s[i].isdigit():
                return False
            i += 1
        return True
if __name__ == "__main__":
    s = Solution()
    string = "123.45e+6"
    print(s.isNumeric(string))
