"""
    >> problem: https://www.acmicpc.net/problem/1715

    >> key: **Keep finding the smallest two cards and sum them up**
        - Must put each sum back to the heap.
        - mistakes: Not [ A + (A+B) + (A+B+C) + ... (A+B+C+D+...+Z) = 26A + 25B + 24C + ... + 1Z ].
            - counter example: [10, 10, 10, 10], ans is 80, not 90.

    >> idea: greedy, min-heap
        - greedy: Should make the locally optimal decision at every step.
        - min-heap: Always add/get the smallest card in O(logn) time.

    >> time-complexity: O(nlogn)
    >> space-complexity: O(n)
"""

import heapq

n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))
# --- O(nlogn)

ans = 0
while len(cards) > 1:
  x = heapq.heappop(cards)
  y = heapq.heappop(cards)
  temp = x + y
  heapq.heappush(cards, temp)
  ans += temp
print(ans)
# --- O(n/2 * 3logn) = O(nlogn)