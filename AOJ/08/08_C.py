import sys
texts = sys.stdin.read().lower()
count = [0]*26
letters = "abcdefghijklmnopqrstuvwxyz"
for x in texts:
    i = 0
    for y in letters:
        if x == y:
            count[i] += 1
        i += 1
for i in range(26):
    print(letters[i] + " : " + str(count[i]))
