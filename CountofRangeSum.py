class Solution:
    def mergeSort(self, nums, helper, start, end, lower, upper):
        res = 0
        if end - start > 1:
            mid = (end + start) // 2
            res += self.mergeSort(helper, nums, start, mid, lower, upper)
            res += self.mergeSort(helper, nums, mid, end, lower, upper)
            small, large, j, k = mid, mid, mid, start
            for i in range(start, mid):
                while small < end and nums[small] - nums[i] < lower: small += 1
                while large < end and nums[large] - nums[i] <= upper: large += 1
                while j < end and nums[j] < nums[i]:
                    helper[k] = nums[j]
                    k += 1
                    j += 1
                res += (large - small)
                helper[k] = nums[i]
                k += 1
        return res
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0] * (1 + len(nums))
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        helper = sums[:]
        res = self.mergeSort(sums, helper, 0, len(sums), lower, upper)
        return res
if __name__ == "__main__":
    s = Solution();
    nums = [-2,0,0,2,2,-2]
    lower = -3
    upper = 1
    res = s.countRangeSum(nums, lower, upper)
    print(res)
