class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        # Run binary search
        arr = self.timemap[key]
        l, r = 0, len(arr) - 1

        while l < r:
            m = l + ((r - l) // 2) + 1

            if arr[m][1] < timestamp:
                l = m

            elif arr[m][1] > timestamp:
                r = m - 1
            
            else:
                return arr[m][0]

        if arr[l][1] > timestamp:
            return ""
        return arr[l][0]
