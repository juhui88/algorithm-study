import heapq


def Lecture_Selector(L, n):
    L.sort()

    room = []
    heapq.heappush(room, L[0][1])

    for i in range(1, n):
        if L[i][0] >= room[0]:  # 두 강의가 겹치지 않는다면
            heapq.heappop(room)
        heapq.heappush(room, L[i][1])

    return len(room)


n = int(input())
L = []

for i in range(n):
    s, t = map(int, input().split())
    L.append((s, t))

print(Lecture_Selector(L, n))
