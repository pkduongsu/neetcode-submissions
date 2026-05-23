class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Input: nums: List[int]
        #Output: output: List[int]
        #Product of all elements of nums except nums[i]

        #Brute force solution that i can think of is just to calculate the product of all elements
        #And divide that by the element at the current index when we iterate through all
        #but then, there will be a case where we divide by 0 -> if thats the case, just calculate the prod 
        #of other elements
        #but how, another loop?
        #skip this approach
        #instead, just use a nested loop and calculate the product of every other element except current pos
        #Time complexity: O(n^2) where n is the length of the input nums array
        #Space: O(n)

        # res = []

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)): 
        #         #cant use i+1 here as we want all the other elements, not elements in front of current element
        #         if i == j:
        #             continue
        #         prod *= nums[j]

        #     res.append(prod)

        # return res

        #Better solution
        #Ex: Input: [1, 2, 3, 4] - Output: [24, 12, 8, 6]
        #With prefix postfix:
        # Prefix: [1, 1, 2, 6] Postfix: [24 , 12, 4, 1] => Final: [1 *24, 1*12, 2*4, 6* 1] (the desired result)
        # We are having 2 extra arrays here, which is not very space efficient
        # so we are just going to store this in 1 res array only, and multiply the element by pre, post
        # initializing the res array with all 1 (neutral) and then we can multiply pref, post

        res = [1] * len(nums)

        prefix = postfix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


