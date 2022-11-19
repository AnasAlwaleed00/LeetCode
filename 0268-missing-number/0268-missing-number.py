class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return ((n * (n+1)) // 2 ) - sum(nums) 

# Get sum of complete series(Gaussian formula) and find the difference between sum of given series