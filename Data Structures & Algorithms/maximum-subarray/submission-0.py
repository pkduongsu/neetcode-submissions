class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0: currentSum = 0
            currentSum += num
            maxSub = max(maxSub, currentSum)
        
        return maxSub