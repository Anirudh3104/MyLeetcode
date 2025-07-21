class TimeMap:

    def __init__(self):
        self.store={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value,timestamp])
        else:
            self.store[key]=[[value,timestamp]]
        return None
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals=self.store[key]
        low,high=0,len(vals)-1
        res=""
        while high>=low:
            mid=(high+low)//2
            if vals[mid][1]==timestamp:
                return vals[mid][0]
            elif vals[mid][1]<timestamp:
                res=vals[mid][0]
                low=mid+1
            else:
                high=mid-1
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)