N = int(input())
flag = False
for g1 in range(N):
    for g2 in range(N):
        for f2 in range(N):
            for f3 in range(N):
                if g1 + g2 * 2 + f2 * 2 + f3 * 3 == N - 1:
                    if g1 + g2 == f2 + f3:
                        print(f2 + f3)
                        flag = True
                        break
                if g1 + g2 * 2 + f2 * 2 + f3 * 3 == N - 2:
                    if g1 + g2 == f2 + f3:
                        print(-1)
                        flag = True
                        break
    if flag:
        break





