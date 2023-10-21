class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {} # Here (index, total) to the number of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[((i, total))] = (backtrack(i + 1, total + nums[i] +
                                          backtrack(i + 1, total + nums[i])))
            return dp[(i, total)]
        return backtrack(0, 0)
    
    # Here the Time Complexity is O(n), using Caching