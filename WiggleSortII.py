from random import randrange
class Solution:
    def __init__(self):
        self.log = []
    def KthLargestNum(self, nums, start, end, k):
        piv = randrange(start, end)
        nums[piv], nums[end - 1] = nums[end - 1], nums[piv]
        pivot = nums[end - 1]
        i = start - 1
        equal = start - 1
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                equal += 1
                if equal > i:
                    nums[equal], nums[j] = nums[j], nums[equal]
            elif nums[j] == pivot:
                equal += 1
                nums[equal], nums[j] = nums[j], nums[equal]
        i_index = i + 1 - start
        equal_index = equal + 1 - start
        print(nums, pivot)
        if i_index < k <= equal_index:
            return nums[equal]
        elif k <= i_index:
            return self.KthLargestNum(nums, start, i + 1, k)
        else:
            return self.KthLargestNum(nums, equal + 1, end, k - equal_index)
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = self.KthLargestNum(nums, 0, length, (length + 1) // 2)
        print(k)
        left, right, i = 0, length - 1, 0
        while i <= right:
            idxMapped = (1 + 2 * i) % (length | 1)
            leftMapped = (1 + 2 * left) % (length | 1)
            rightMapped = (1 + 2 * right) % (length | 1)
            if nums[idxMapped] > k:
                nums[idxMapped], nums[leftMapped] = nums[leftMapped], nums[idxMapped]
                left += 1
                i += 1
            elif nums[idxMapped] < k:
                nums[idxMapped], nums[rightMapped] = nums[rightMapped], nums[idxMapped]
                right -= 1
            else:
                i += 1
if __name__ == "__main__":
    s = Solution();
    nums = [5,3,1,2,6,7,8,5,5]
    s.wiggleSort(nums)
    print(nums)
