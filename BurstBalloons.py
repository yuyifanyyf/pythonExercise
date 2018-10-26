class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for x in range(n + 1)] for y in range(n + 1)]
        nums.append(1)
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                left, right = i, i + k - 1
                for j in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[j] * nums[j - 1] * nums[j + 1] + dp[left][j - 1] + dp[j + 1][right])
        return dp[0][-2]
if __name__ == "__main__":
    s = Solution()
    nums = [3,1,5,8]
    print(s.maxCoins(nums))
