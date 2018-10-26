class Solution:
    def ReverseSentence(self, s):
        # write code heres
        if not s:
            return s
        wList = s.split()
        wList.reverse()
        return " ".join(wList) if wList else " "
if __name__ == "__main__":
    s = Solution()
    string = "1 2 3"
    print(s.ReverseSentence(string))
