class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        pair.sort(reverse=True, key=lambda x: x[0]) 
        fleet_count = 0  
        slowest_time = 0.0
        for i in pair:
            time = (target - i[0]) / i[1]
            if time > slowest_time:
                fleet_count += 1
                slowest_time = time
        return fleet_count

        
        