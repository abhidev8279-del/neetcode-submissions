class MyHashMap:

    def __init__(self):
        self.a = []
        self.b = []
        

    def put(self, key: int, value: int) -> None:
        a1 = str(key)
        if a1 in self.a:
            self.b[self.a.index(a1)] = str(value)
        self.a.append(a1)
        self.b.append(str(value))

    def get(self, key: int) -> int:
        a1 = str(key)
        if a1 not in self.a:
            return -1
        return int(self.b[self.a.index(a1)])

    def remove(self, key: int) -> None:
        a1 = str(key)
        if a1 not in self.a:
            return None
        while a1 in self.a:
            self.b.remove(self.b[self.a.index(a1)])
            self.a.remove(a1)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)