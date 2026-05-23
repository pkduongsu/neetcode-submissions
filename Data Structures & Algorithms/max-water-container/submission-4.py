class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #define in the problem: output is the maximum area that we can achieve
        #Area of a rectangle: height * width
        #height: constrained by the lower bar -> get the lower bar using min func
        #width: distance between 2 bars -> index of the further, rightmost bar - index of leftmost one (or just use abs)
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                currentArea = min(heights[i], heights[j]) * (j - i)
                maxArea = max(maxArea, currentArea)

        return maxArea
