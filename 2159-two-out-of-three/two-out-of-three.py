class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hm = {}
        for n in set(nums1):
            hm[n] = hm.get(n,0) + 1
        for n in set(nums2):
            hm[n] = hm.get(n,0) + 1
        for n in set(nums3):
            hm[n] = hm.get(n,0) + 1
        res = []
        for key, val in hm.items():
            if val > 1:
                res.append(key)
        return res