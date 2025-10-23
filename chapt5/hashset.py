
# void add(key)
# bool contains(key)
# void remove(key)

class MyHashSet:
    def __init__(self):
        self.set = set()
 
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.add(key)
 
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)
        else:
            return "Key not in set."
    def contains(self, key: int) -> bool:
        return key in self.set
            
 
 
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(2)
obj.add(5)
obj.add(7)
print(obj.set)
obj.remove(5)
param_3 = obj.contains(5)
print(param_3)
print(obj.set)
