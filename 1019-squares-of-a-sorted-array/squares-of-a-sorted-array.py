class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                new_nums[i] = nums[left] ** 2
                left += 1
            else:
                new_nums[i] = nums[right] ** 2
                right -= 1
                    
        return new_nums