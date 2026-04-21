import hashlib

class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __eq__(self, n: Node):
        return self.key == n.key

    
def string_to_hash(s: str) -> int:
    return int.from_bytes(hashlib.sha256(s.encode('utf-8')).digest(),"big")


class SeparateChaining:
    def __init__(self, size: int = 1):
        self.hashtable = [[] for _ in range(size)]
        self.size = size
    
    def exists(self, key: str) -> bool:
        h = string_to_hash(key) % self.size
        for elem in self.hashtable[h]:
            if key == elem.key:
                return True
        return False

    def remove(self, key: str):
        h = string_to_hash(key) % self.size
        for elem in self.hashtable[h]:
            if elem.key == key:
                if elem.value > 1:
                    elem.value -= 1
                else:
                    self.hashtable[h].remove(elem)
                self.rearrange()
                return

    def insert(self, key: str): 
        h = string_to_hash(key) % self.size

        for a in self.hashtable[h]:
            if a.key == key:
                a.value += 1
                return
        self.hashtable[h].append(Node(key, 1))
        self.rearrange()

    def private_insert(self, n: Node) :
        h = string_to_hash(n.key) % self.size
        self.hashtable[h].append(n)

    def alpha(self): 
        n = 0
        m = self.size
        for a in self.hashtable:
            n += len(a)
        return n/m

    def rearrange(self): 
        a = self.alpha()

        #Increase size of list
        if a > 1:
            self._resize(self.size * 2)

        #Decrease size of list
        elif a < 0.25 and self.size > 1:
            self._resize(self.size // 2)
        else: return

    def _resize(self, new_size):
        oldtable = self.hashtable
        self.size = new_size
        self.hashtable = [[] for _ in range(new_size)]
        for hink in oldtable:
            for elem in hink:
                self.private_insert(elem)
    def items(self):
        for bucket in self.hashtable:
            for node in bucket:
                yield node.key, node.value
            
        

