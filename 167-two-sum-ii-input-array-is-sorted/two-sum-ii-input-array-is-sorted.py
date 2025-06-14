class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i , j= 0,len(numbers) - 1
        while i < j:
            currentSum=numbers[i] + numbers[j]
            if  currentSum < target:
                i +=1
            elif currentSum > target:
                j -=1
            else:
               return [i+1, j+1] 