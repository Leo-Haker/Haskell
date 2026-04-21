from __future__ import annotations
import hashlib

"""
Att byta till hash(s) istället för sha256 gör 
att det tar 1/6 av tiden. Från 31 minuter och 8 sekunder 
till 5 minuter och 54 sekunder.
Att lägga till en count för varje element istället 
för att räkna alla element varje gång alpha() kallas
gör att vi går från 5 minuter och 54 sekunder till 17 sekunder.
Göra om Remove så att den inte kallas exit() 
gör att vi går från 17 sekunder till 12 sekunder.


Svar:
10.1 Rearrange() tar längst tid. 
om hashtabellen inte är balanserad, stort alpha, 
då tar alla sökningar och insättningar längre tid. 

10.2 Använda bit and operation istället för modulus. Alltså 
ska size vara en potens av 2.  

Run 100 done
testReference.py   avg: 12.238s
test1Reference.py  avg: 13.090s

Tog bort extra functioner och gör uttryckern direkt,
ingaa Extract method.

Run 100 done
testReference.py   avg: 11.748s
test1Reference.py  avg: 10.697s
"""

class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __eq__(self, n: Node):
        return self.key == n.key

    


class SeparateChaining:
    def __init__(self, size: int = 1):
        self.hashtable = [[] for _ in range(size)]
        self.size = size
        self.count = 0
    
    def exists(self, key: str) -> bool:
        h = hash(key) & (self.size - 1)
        for elem in self.hashtable[h]:
            if key == elem.key:
                return True
        return False
    
    def remove(self, key: str):
        h = hash(key) & (self.size - 1)
        for elem in self.hashtable[h]:
            if elem.key == key:
                self.hashtable[h].remove(elem)
                self.count -= 1
                self.rearrange()
                return
            
    def insert(self, key: str, value: int = 1): 
        index = hash(key) & (self.size - 1)

        for node in self.hashtable[index]:
            if node.key == key:
                node.value = value
                return
        self.hashtable[index].append(Node(key, value))
        self.count += 1
        self.rearrange()   


    def private_insert(self, n: Node) :
        h = hash(n.key) & (self.size - 1)
        self.hashtable[h].append(n)

    def alpha(self): 
        return self.count / self.size
    
    def get (self, key: str) -> int:
        index = hash(key) & (self.size - 1)
        for elem in self.hashtable[index]:
            if elem.key == key:
                return elem.value
        raise KeyError("Key not found")

    def rearrange(self): 
        a = self.alpha()

        #Increase size of list
        if a > 1:
            self.resize(self.size << 1)

        #Decrease size of list
        elif a < 0.25 and self.size > 1:
            self.resize(self.size >> 1)
        else: return

    def resize(self, new_size):
        oldtable = self.hashtable
        self.size = new_size
        self.hashtable = [[] for _ in range(self.size)]
        for hink in oldtable:
            for elem in hink:
                self.private_insert(elem)
    
    def items(self):
        for bucket in self.hashtable:
            for node in bucket:
                yield node.key, node.value
            
