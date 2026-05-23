class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #initialize a count of characters (26 characters in the alphabet) array for each string
            for char in s:
                #update the count of each char in the count
                #we map indexes to characters (ex: 0 - a, 25 - z)
                #we can do that by calculating the offset between current char ASCII value with char a
                count[ord(char) - ord("a")] += 1

            #after we got the count for each char, we use that as the dict key
            #in python, list cannot be keys -> convert to tuple
            res[tuple(count)].append(s)

        return list(res.values())



                    
