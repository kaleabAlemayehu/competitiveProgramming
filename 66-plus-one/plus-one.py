class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1
        if digits[l] != 9: 
            digits[l] += 1
            return digits
        re = 0
        while digits[l] == 9:
            digits[l] = 0
            re = 1
            l-=1
        if re == 1:
            if digits[0] == 0:
                digits.append(0)
                if l < 0:
                    l = 0
                digits[l] = 1
            else:
                if l < 0:
                    l = 0
                digits[l] += re
        return digits
            
        