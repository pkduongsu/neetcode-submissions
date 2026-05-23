class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string s
        #output: length of the longest substring without repeating characters - int
        #def lenghtofLongestSub(s: str) - > int:

        #brute force:
        #to have a list to track the characters that we went through
        #if there is a duplicate character, stop
        #find the length
        #and keep a variable to track the maximum length we can achieve for non-repeating characters

        maxLen = 0

        for i in range(len(s)):
            subStr = []
            for j in range(i, len(s)):
                if s[j] in subStr:
                    break
                subStr.append(s[j])
            maxLen = max(maxLen, len(subStr))
        return maxLen

        