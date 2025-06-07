class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ft = Counter(t)
        fs = Counter(s)
        for key, val in ft.items():
            if key in ft and not (key in fs):
                return key
            if val != fs.get(key):
                return key

        