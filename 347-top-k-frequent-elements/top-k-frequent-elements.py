class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        buck = [[]for i in range(len(nums)+1)]
        for key, value in hm.items():
            buck[value].append(key)
        res = []
        for i in range(len(buck)-1, 0, -1):
            for n in buck[i]:
                res.append(n)
                if len(res) == k:
                    return res

        