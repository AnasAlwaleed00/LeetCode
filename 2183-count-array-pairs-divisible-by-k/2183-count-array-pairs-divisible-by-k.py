class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ans = 0
        n = len(nums)
        
        for i in range(n):
            x = math.gcd(k,nums[i])
            want = k // x
            for num in counter:
                if num % want == 0:
                    ans += counter[num]
            counter[x] += 1
        return ans