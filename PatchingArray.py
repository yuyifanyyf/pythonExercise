class Solution:
    def getKSum(self, base, nums, start, k, lastSum, sums):
        if k == 0:
            if base + lastSum - 1 < len(sums):
                sums[base + lastSum - 1] = True
        else:
            for i in range(start, len(nums) - k + 1):
                self.getKSum(base, nums, i + 1, k - 1, lastSum + nums[i], sums)
    def update(self, nums, cur):
        while cur < len(nums) and nums[cur]:
            cur += 1
        return cur
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        sums = [False for x in range(n)]
        for i in range(1, len(nums) + 1):
            self.getKSum(0, nums, 0, i, 0, sums)
        cur = self.update(sums, 0)
        res = 0
        while cur < len(sums):
            res += 1
            sums[cur] = True
            for k in range(1, len(nums) + 1):
                self.getKSum(cur + 1, nums, 0, k, 0, sums)
            nums.append(cur + 1)
            cur = self.update(sums, cur)
        return res
if __name__ == "__main__":
    s = Solution()
    nums = []
    n = 7
    res = s.minPatches(nums, n)
    print(res)
