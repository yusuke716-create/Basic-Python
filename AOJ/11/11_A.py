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


saikoro = list(map(int, input().split()))
texts = list(input())

dice = Dice(saikoro)

for i in texts:
    if i == "E":
        dice.turn_e()
    if i == "N":
        dice.turn_n()
    if i == "S":
        dice.turn_s()
    if i == "W":
        dice.turn_w()

print(dice.show_top())
