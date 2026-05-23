class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        #will the strings will always be lowercase?
        #if not, convert
        for i in range(len(strs)):
            count = [0] * 26 
            for c in strs[i]:
                count[ord(c) - ord('a')] += 1

            hashMap[tuple(count)].append(strs[i])
        return list(hashMap.values())

        # Time complexity: O(n * m), where n is length of input strs array
        # m: length of longest word in strs array 

        #Space: O(n * m)