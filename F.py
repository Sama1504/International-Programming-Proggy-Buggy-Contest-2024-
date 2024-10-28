import sys

input = sys.stdin.read

data = input().split()
N = int(data[0])
B = int(data[1])
E = int(data[2])

meetings = []
index = 3
for _ in range(N):
    s = int(data[index])
    f = int(data[index + 1])
    meetings.append((s, f))
    index += 2

meetings.sort()

free_time = 0
current_time = B

for s, f in meetings:
    if s > E:
        break
    if s > current_time:
        free_time += min(s, E) - current_time
    current_time = max(current_time, f)

if current_time < E:
    free_time += E - current_time

print(free_time)