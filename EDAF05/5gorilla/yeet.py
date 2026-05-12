import sys

characters = sys.stdin.buffer.readline().decode().strip().replace(" ", "")

data = sys.stdin.buffer.read().split()


cost_pair = []
idx = 0
length  = len(characters)

for n in range(length):
    row = [int(p) for p in data[idx: idx + length]]
    idx += length
    cost_pair.append(row)

number_quiries = data[idx]; idx += 1

list_quiries = []

for n in number_quiries:
    list_quiries.append((data[idx].decode(), data[idx+1].decode()))
    idx += 2

print(characters)
print(cost_pair)
print(list_quiries)