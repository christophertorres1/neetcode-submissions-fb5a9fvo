class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times_to_dest = [(target - pos) / spd for pos, spd in cars]

        stack = []
        for time in times_to_dest:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        
        return len(stack)
        
            