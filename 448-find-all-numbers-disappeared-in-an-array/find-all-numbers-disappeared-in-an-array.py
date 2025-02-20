class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_nums = []
        set_nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                new_nums.append(i)
        return new_nums