class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currentMax = 0
        
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                #area of rect: width * height
                currentArea = min(heights[i], heights[j]) * (j - i)
                currentMax = max(currentMax, currentArea)

        print(currentMax)
        return currentMax