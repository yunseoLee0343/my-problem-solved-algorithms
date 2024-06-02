"""
    >> problem: https://www.acmicpc.net/problem/1339

    >> constraints:
        1. 1 <= N <= 10
        2. 1 <= len(word) <= 8
            Uniqueness of each word is guaranteed.
        3. Word consists of uppercase English letters.

    >> key: **Allocating a unique number to all alphabets located in same index.**
        - mistakes: Too simply thought about. Assigning the largest number to the most frequent alphabet is not always the best choice.
            - counter example: [10, ABB, BB, BB, BB, BB, BB, BB, BB, BB, BB]

    >> idea: greedy
        - greedy: Should make the locally optimal decision at every step.

    >> time-complexity: O(nlogn)
    >> space-complexity: O(n)
"""

"""
****** Wrong Trial ******

n = int(input())
words = []
matrix = [[-1 for _ in range(8)] for _ in range(10)]
alphabets = [-1]*26

for i in range(n):
    word = input()
    words.append(word)
    for j in range(len(word)):
        matrix[i][7-j] = ord(word[len(word) - j - 1]) - 65
# --- O(n*8)

temp = 9
ans = 0
for i in range(8):
    for j in range(n):
        if matrix[j][i] == -1:
            continue
        elif alphabets[matrix[j][i]] == -1:
            alphabets[matrix[j][i]] = temp
            temp -= 1
        ans += alphabets[matrix[j][i]] * (10 ** (7 - i))
print(ans)
# --- O(8*n)
"""

import sys

n = int(input())
S = [sys.stdin.readline().strip() for _ in range(n)]
words = {}

for s in S:
    x = len(s) - 1
    for i in s:
        if i in words:
            words[i] += 10 ** x
        else:
            words[i] = 10 ** x
        x -= 1
# --- O(n*8)

words_sort = sorted(words.values(), reverse=True)
ans = 0
temp = 9
for i in words_sort:
    ans += temp * i
    temp -= 1
print(ans)
# --- O(nlogn) + O(n) = O(nlogn)

