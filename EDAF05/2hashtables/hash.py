import hashlib
from collections import deque

def string_to_hash(s: str) -> int:
    return int.from_bytes(hashlib.sha256(s.encode('utf-8')).digest(),"big")

def main():
    a = "hej"
    print(a)
    print(string_to_hash(a))
    print("hejsan")

class SeparateChaining:
    def __init__(self):
        self.hashtable = [[]]
        self.size = 1
    
    def insert(self, n: Node): 
        hashKey = string_to_hash(n.key)
        hash = self.size % hashKey
        self.hashtable[hash].append(Node)
        self.rearrange()

    def private_insert(self, n: Node) :
        hash = self.size % n.key
        self.hashtable[hash].append(Node)

    def alpha(self): 
        n = 0
        m = self.size
        for a in self.hashtable:
            n += len(a)
        return n/m

    def rearrange(self): 
        if self.alpha < 1:
            self.size += 1
            oldtable = self.hashtable
            self.hashtable = [[] for _ in range(self.size)]
            for a in oldtable:
                for b in a:
                    self.private_insert(b)
        else:
            return
        

class Node: 
    def __init__(self, value):
        self.key = string_to_hash(value)
        self.value = value
        

a = [Node]
        


if __name__ == "__main__":
    a = main
    a()
