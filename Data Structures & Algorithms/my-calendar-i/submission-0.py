class MyCalendar:
    
    def __init__(self):
        self.myCal={}
        

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(startTime, endTime):
            if i in self.myCal:
                return False
        
        for i in range(startTime, endTime):
            self.myCal[i]=-1
      
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)