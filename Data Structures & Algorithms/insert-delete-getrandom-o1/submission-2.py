class RandomizedSet:

    def __init__(self):
        self.myList=[]
        self.myMap={}
        

    def insert(self, val: int) -> bool:
        if val in self.myMap:
            return False
        else:
            self.myList.append(val)
            self.myMap[val]=len(self.myList)-1
            
            return True

        

    def remove(self, val: int) -> bool:
        if val in self.myMap:
            idx=self.myMap[val]
            lastElem=self.myList[-1]
            self.myList[idx]=lastElem
            self.myMap[lastElem]=idx
            self.myList.pop()
            del self.myMap[val]
            return True
        else:
            return False

            
        

    def getRandom(self) -> int:
      
        return (random.choice(self.myList))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()