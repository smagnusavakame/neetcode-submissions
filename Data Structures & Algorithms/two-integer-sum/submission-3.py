class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        itr = len(nums)
        for i in range(itr):
            for j in range(i + 1, itr):
                if nums[i] + nums[j] == target:
                    return [i, j]