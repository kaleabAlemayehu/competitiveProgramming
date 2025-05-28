class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hm = {}
        nums1 =set(nums1) 
        nums2 =set(nums2) 
        nums3 =set(nums3) 
        for n in nums1:
            hm[n] = hm.get(n,0) + 1
        for n in nums2:
            hm[n] = hm.get(n,0) + 1
        for n in nums3:
            hm[n] = hm.get(n,0) + 1
        resSet =set() 
        for key, val in hm.items():
            if val > 1:
                resSet.add(key)
        return list(resSet)