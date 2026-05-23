class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       #input: string s
       #output: length of the longest substring without any duplicates -> integer
       #define function: lengthOfLongestSubstring(s: str) -> int:

       #test 1: input: zxyzxyz -> output: 3
       #test 2: input: abcdab -> output: 4
       #test 3: input: xxxx -> output: 1

       #brute force approach:
       #loop through each character
       #set() 
       #loop through the remaining characters for the current char we're at
       #see the longest possible sequence that we can form with that char
       #variable to store the max length and update that by comparing the current max length and the 
       #stored max length
       #finally, return maxLength

       maxLength = 0
       #question: constraint -> 0 <= s.length <= ...
       for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            maxLength = max(maxLength, len(charSet))

       return maxLength

       
