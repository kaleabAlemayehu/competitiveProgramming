class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if (i/2 in arr or i*2 in arr )and i != 0:
                print(i)
                return True
            if i == 0:
                temp = arr
                temp.remove(0) 
                if i/2 in temp or i*2 in temp:
                    return True
                
        return False
        