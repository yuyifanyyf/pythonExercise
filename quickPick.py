class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quickPick(nums, start, end, k):
            if end - start < k: return []
            piv = nums[start]
            mid = start
            for i in range(start + 1, end):
                if nums[i] <= piv:
                    mid += 1
                    nums[mid], nums[i] = nums[i], nums[mid]
            if mid + 1 - start > k:
                return quickPick(nums, start + 1, mid + 1, k)
            elif mid + 1 - start == k:
                return nums[start:mid + 1]
            else:
                return nums[start:mid + 1] + quickPick(nums, mid + 1, end, k - (mid + 1 - start))
        start, end = 0, len(tinput)
        res = quickPick(tinput, start, end, k)
        return sorted(res)
if __name__ == "__main__":
    s = Solution()
    nums = [4,5,1,6,2,7,3,8]
    k = 1
    print(s.GetLeastNumbers_Solution(nums, k))
