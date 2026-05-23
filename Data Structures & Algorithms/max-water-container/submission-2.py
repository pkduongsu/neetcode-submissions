class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                currentArea = (j - i) * min(heights[i], heights[j])
                maxArea = max(maxArea, currentArea)

        return maxArea


