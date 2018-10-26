# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.summation = 0
#         self.dup = 1
#         self.left = None
#         self.right = None
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for i in nums]
        num = [(nums[i], i) for i in range(len(nums))]
        helper = [(nums[i], i) for i in range(len(nums))]
        def mergeSort(nums, helper, start, end, res):
            if end - start > 1:
                mid = (start + end) // 2
                mergeSort(helper, nums, start, mid, res)
                mergeSort(helper, nums, mid, end, res)
                #merge = [0 for i in range(end - start)]
                i, j, k = start, mid, 0
                while i < mid and j < end:
                    if nums[i] <= nums[j]:
                        res[nums[i][1]] += (j - mid)
                        helper[k + start] = nums[i]
                        i += 1
                    else:
                        helper[k + start] = nums[j]
                        j += 1
                    k += 1
                while i < mid:
                    res[nums[i][1]] += (j - mid)
                    helper[k + start] = nums[i]
                    i += 1
                    k += 1
                while j < end:
                    helper[k + start] = nums[j]
                    j += 1
                    k += 1
        mergeSort(num, helper, 0, len(num), res)
        return res
if __name__ == "__main__":
    s = Solution();
    nums = [5,2,6,1]
    print(s.countSmaller(nums))
