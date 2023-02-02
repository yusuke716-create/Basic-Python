count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
for a in range(n):
    b, f, r, v = list(map(int, input().split()))
    count[b - 1][f - 1][r - 1] += v
for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" {}".format(count[i][j][k]), end = "")
        print()
    if i != 3:
        print("####################")
