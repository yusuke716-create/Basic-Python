s = int(input())
h = s // 3600
m = s % 3600 // 60
s = s % 3600 % 60
print(f"{h}:{m}:{s}")
