class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #define in the problem: output is the maximum area that we can achieve
        #Area of a rectangle: height * width
        #height: constrained by the lower bar -> get the lower bar using min func
        #width: distance between 2 bars -> index of the further, rightmost bar - index of leftmost one (or just use abs)
        #Brute force: traverse through every possible pair to find max area
        #Optimal: traverse from both sides of the array using 2 pointers, l and r
        #Understands what impacts the area: height
        #See that the bar with lower height can limit the height of higher bar, hence lower possible area
        #-> if thats the case, move either right or left pointer to discover chances of higher height bars
        l, r = 0, (len(heights) - 1)
        maxArea = 0

        while l < r: #should not overlap since bars should be unique 
            currentArea = (r - l) * min(heights[l], heights[r])
            maxArea = max(maxArea, currentArea)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: #equal -> can move anywhere
                l += 1
            
        return maxArea