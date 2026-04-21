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
    


if __name__ == "__main__":
    a = main
    a()
