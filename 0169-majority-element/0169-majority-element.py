class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = Counter(nums)
        n = len(nums)
        for num in nums:
            if numsMap[num] > n // 2: return num