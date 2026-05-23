class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            res[sortedString].append(strs[i])


        return list(res.values())



                    
