class Dice:
    def __init__(self, num):
        self._1 = num[0]
        self._2 = num[1]
        self._3 = num[2]
        self._4 = num[3]
        self._5 = num[4]
        self._6 = num[5]

    def turn_e(self):
        self._1, self._3, self._4, self._6 = self._4, self._1, self._6, self._3

    def turn_w(self):
        self._1, self._3, self._4, self._6 = self._3, self._6, self._1, self._4

    def turn_n(self):
        self._1, self._2, self._5, self._6 = self._2, self._6, self._1, self._5

    def turn_s(self):
        self._1, self._2, self._5, self._6 = self._5, self._1, self._6, self._2

    def show_top(self):
        return self._1

    def same_saikoro(self, fig):
        if (self._1 == fig[0] and self._2 == fig[1] and self._3 == fig[2] and
           self._4 == fig[3] and self._5 == fig[4] and self._6 == fig[5]):
            return True

    def same_one(self, fig):
        for i in range(2):
            for j in range(3):
                for k in range(4):
                    if self.same_saikoro(fig):
                        return True
                    self.turn_e()
                self.turn_s()
            self.turn_w()
            self.turn_n()
        return False


n = int(input())
saikoro = []
for i in range(n):
    saikoro.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(saikoro[i])
        if dice.same_one(saikoro[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')
