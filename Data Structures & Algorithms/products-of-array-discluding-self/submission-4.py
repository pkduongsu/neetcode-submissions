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
        
        res = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)): 
                #cant use i+1 here as we want all the other elements, not elements in front of current element
                if i == j:
                    continue
                prod *=  nums[j]

            res.append(prod)

        return res