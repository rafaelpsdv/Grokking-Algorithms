



class MyHashMap:
 
    def __init__(self):
        self.hashmap = {}
 
    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
 
    def get(self, key: int) -> int:
        if key in self.hashmap:
            return self.hashmap[key]
        return -1
 
    def remove(self, key: int) -> None:
        if key in self.hashmap:
            self.hashmap.pop(key)

 
 
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 'oi')
obj.put(2, 'tchau')
param_2 = obj.get(1)
print(obj.hashmap)
obj.remove(1)
print(obj.hashmap)