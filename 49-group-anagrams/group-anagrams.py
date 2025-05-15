class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm =defaultdict(list) 
        for val in strs:
            key= [0]*26
            for s in val:
                key[ord(s)- ord('a')] += 1
            hm[tuple(key)].append(val)
        return hm.values()
                
        
        