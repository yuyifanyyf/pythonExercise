class Solution:
    def match(self, s, pattern):
        # write code here
        dp = [[False for i in range(len(s) + 1)] for j in range(len(pattern) + 1)]
        dp[0][0] = True
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if pattern[i - 1] == "*":
                    if (i - 2 >=0 and dp[i-2][j]) or (j - 1 >= 0 and dp[i][j-1] and (pattern[i-2] == s[j-1] or pattern[i-2]==".")):
                        dp[i][j] = True
                elif i-1>=0 and j-1>=0 and (pattern[i-1] == "." or pattern[i-1] == s[j-1]) and dp[i-1][j-1]:
                    dp[i][j] = True
        return dp[-1][-1]
if __name__ == "__main__":
    s = Solution()
    string = "a"
    pattern = ".*"
    print(s.match(string, pattern))
