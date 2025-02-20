class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        count = 0

        for i in range(len(nums)):
            sum1 = sum(nums[:i])
            sum2 = sum(nums[i+1:])
            if sum1 == sum2:
                count += 1
                return i
        if count == 0:
            return -1