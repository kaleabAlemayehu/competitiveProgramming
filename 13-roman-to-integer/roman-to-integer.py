class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0
        i = 0
        while i < len(s):
            if s[i] == "I" and i < len(s) - 1:
                if s[i+1] == "V":
                    sum += 4
                    i+=2
                    continue
                if s[i+1]  == "X":
                    sum +=9
                    i+=2
                    continue
            if s[i] == "X" and i < len(s) - 1:
                if s[i+1] == "L":
                    sum += 40
                    i+=2
                    continue
                if s[i+1] == "C":
                    sum += 90
                    i+=2
                    continue
            if s[i] == "C" and i < len(s) - 1:
                if s[i+1] == "D":
                    sum += 400
                    i+=2
                    continue
                if s[i+1] == "M":
                    sum += 900
                    i+=2
                    continue
            sum += pair[s[i]]
            i+=1
        return  sum
            