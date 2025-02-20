class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = 0

        for i in nums:
            if i * 2 <= max_num:
                count += 1
        return -1 if count != len(nums) - 1 else nums.index(max_num)