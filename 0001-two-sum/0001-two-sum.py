class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            neededNum = target - nums[i]
            if neededNum in prevMap:
                return [i, prevMap[neededNum]]
            prevMap[nums[i]] = i