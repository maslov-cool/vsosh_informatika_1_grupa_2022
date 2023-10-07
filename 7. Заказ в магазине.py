import math

N = [i for i in range(1, int(input()) + 1)]
M = int(input())

if sum(N) < M:
    print(0)
else:
    A = []
    for i in range(math.ceil(len(N) / 2)):
        el = [N[i]]
        flag = False
        for j in range(len(N) - 1, -1, -1):
            if N[j] not in el:
                if sum(el) + N[j] > M:
                    continue
                elif sum(el) + N[j] == M:
                    el.append(N[j])
                    flag = True
                    break
                else:
                    el.append(N[j])
        if flag:
            A.append(el)

    print(*sorted(min(A, key=lambda x: x[0])), sep='\n')














