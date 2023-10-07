import math
n, k = int(input()), int(input())
print((k + 1) // 2 if k % 2 != 0 else k // 2 + math.ceil(n / 2))