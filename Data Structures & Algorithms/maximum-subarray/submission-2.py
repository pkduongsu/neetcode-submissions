class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                maxSum = max(maxSum, current)

        return maxSum
        
        

