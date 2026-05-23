class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashAn = defaultdict(list)
        res = []



        for i in range(len(strs)):
            countC = [0] * 26 #[a, b, c]
            for char in strs[i]:
                countC[ord(char) - ord('a')] += 1
            hashAn[tuple(countC)].append(strs[i])

        
        return list(hashAn.values())

        
            




                    
