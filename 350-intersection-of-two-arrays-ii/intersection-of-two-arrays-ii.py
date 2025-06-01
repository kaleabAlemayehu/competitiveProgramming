class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fq1 = Counter(nums1)
        fq2 = Counter(nums2)
        output = []
        for key, val in fq1.items():
            if key in fq2:
               output.extend([key] * min(val, fq2.get(key)))
        return output 


        
        