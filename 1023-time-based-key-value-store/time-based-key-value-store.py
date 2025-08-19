class TimeMap:

    def __init__(self):
        self.values = {} # key: values ( timestamp, value)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values.setdefault(key, []).append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        temp = self.values.get(key, [])
        l, r = 0, len(temp) - 1
        while l <= r :
            m = l + (r - l) // 2
            if temp[m][0] == timestamp:
                return temp[m][1]
            if temp[m][0] < timestamp:
                res = temp[m][1]
                l = m + 1
            else:
                r = m - 1
        return res 

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)