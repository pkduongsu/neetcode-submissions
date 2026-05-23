class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                maxProd = max(maxProd, prod)

        return maxProd
        