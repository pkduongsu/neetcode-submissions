class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap to store:
        # key: sorted value of the string 
        # value: original value of the string, which is a list 

        # then go through every values in the dict to return final result

        #Time: O(n * mlogm), where n is the length of initial strs 
        # m is the length of the longest word 

        #Space: O(n * m)?
        
        anal = defaultdict(list)

        for i in range(len(strs)):
            current = str(sorted(strs[i]))
            anal[current].append(strs[i])

        result = []

        for i in anal:
            result.append(anal[i])

        return result