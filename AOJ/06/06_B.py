cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]
a = int(input())
for b in range(a):
    ch, rank = input().split()
    rank = int(rank)
    cards[pattern.index(ch)][rank - 1] = True
for i in range(0, 4):
    for j in range(0, 13):
        if cards[i][j] is False:
            print(pattern[i], j + 1)
