class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hm = defaultdict(int)
        for c in s:  
            hm[c]+=1
        cnt =  hm[s[0]]
        for key, count in hm.items():
            if cnt != count:
                return False
        return True
        