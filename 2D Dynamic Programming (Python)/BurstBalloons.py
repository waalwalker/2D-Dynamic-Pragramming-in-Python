class Solution:
    def burstBalloons(self, nums: list[int]) -> int:
        # Aim is Max Coins
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r), coins])
            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)

# This Dynamic Problem has Time Complexity of O(n ^ 3),
# and, has the Memory Complexity of O(n ^ 2)
# Here we will use the brute force approach and Depth first search