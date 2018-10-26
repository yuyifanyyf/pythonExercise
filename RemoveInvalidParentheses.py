class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strList = list(s)
        res = []
        def remove(s, startIndex, lastRemove, res, left, right, flag):
            count = 0
            while startIndex < len(s):
                c = s[startIndex]
                if c == left: count += 1
                elif c == right: count -= 1
                if count < 0: break
                else: startIndex += 1
            if count < 0:
                for i in range(lastRemove + 1, startIndex + 1):
                    if s[i] == right and (i - 1 == lastRemove or s[i - 1] != right):
                        s[i] = ""
                        remove(s, startIndex + 1, i, res, left, right, flag)
                        s[i] = right
            elif flag:
                s.reverse()
                remove(s, 0, -1, res, right, left, False)
            else:
                s.reverse()
                res.append(''.join(s))
                s.reverse()
        remove(strList, 0, -1, res, "(", ")", True)
        return res
if __name__ == "__main__":
    s = Solution()
    string = "(((k()(("
    print(s.removeInvalidParentheses(string))
