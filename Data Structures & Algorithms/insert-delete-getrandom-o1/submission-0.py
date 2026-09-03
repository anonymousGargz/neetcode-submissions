class RandomizedSet:

    def __init__(self):
        self.mySet=set()

    def insert(self, val: int) -> bool:
        if val in self.mySet:
            return False
        else:
            self.mySet.add(val)
            return True

        

    def remove(self, val: int) -> bool:
        if val in self.mySet:
            self.mySet.remove(val)
        

    def getRandom(self) -> int:
        myList=list(self.mySet)
        randomIndex=random.random()*len(myList)
        return (myList[int(randomIndex)])
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()