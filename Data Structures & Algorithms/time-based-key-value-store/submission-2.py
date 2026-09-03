class TimeMap:

    def __init__(self):
        self.myDict={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[(key, timestamp)]=value

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp, -1, -1):
            if (key, i) in self.myDict:
                return (self.myDict[(key, i)])
        return ""

        
