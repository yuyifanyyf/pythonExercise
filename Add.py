# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while True:
            Sum = num1 ^ num2
            carry = num1 & num2
            if not carry:
                return Sum
            num1 = Sum
            num2 = carry
if __name__ == "__main__":
    s = Solution()
    print(s.Add(100,100))
