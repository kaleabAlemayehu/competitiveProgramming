class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i <= j:
            osi = ord(s[i])
            osj = ord(s[j])
            if (osi < ord('a') or osi > ord('z')) and not (osi >= ord('0') and osi <= ord('9')):
                i+=1
                continue
            if (osj < ord('a') or osj > ord('z')) and not (osj >= ord('0') and osj <= ord('9')):
                j-=1
                continue
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
                continue
        return True

            

            

        