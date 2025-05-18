class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[1, 2, 3, 5, 2, 1, 1]
        #          i        j
        #[1, 1, 1, 2, 2, 3, 5]
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] >= nums[j]:
                j+=1
                continue
            if nums[i] < nums[j]:
                if nums[i+1] < nums[j]:
                    i+=1
                    nums[i], nums[j] = nums[j], nums[i]
                    j+=1
                else:
                    i+=1
                    j+=1
                continue
        return len(nums[0:i+1])
            
        