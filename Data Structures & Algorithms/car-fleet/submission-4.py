class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        time_to_dest = [(target - pos) / spd for pos, spd in pairs]

        fleets = []
        for time in time_to_dest:
            while fleets and time >= fleets[-1]:
                fleets.pop()
            fleets.append(time)
        
        return len(fleets)
