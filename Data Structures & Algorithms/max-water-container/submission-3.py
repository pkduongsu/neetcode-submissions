class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, (len(heights) - 1)
        maxArea = 0

        while l < r:
            currentArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, currentArea)
            
            if (heights[l] < heights[r]):
                l = l + 1
            elif (heights[r] < heights[l]):
                r = r - 1
            else: 
                l = l + 1

        return maxArea


