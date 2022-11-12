import os

class XO:
    occupied = [" " for _ in range(9)]
    winner = None
    leng = 0
    def __init__(self, name):
        self.name = name
        self.vis = []
    
    def play(self):
        print("\n\t{}'s Turn:".format(self.name), end = "")
        n = int(input())
        if XO.occupied[n-1] != " ":
            print("Wrong Input, Enter correctly")
            self.play()
            return
        self.vis.append(n)
        XO.occupied[n-1] = self.name
        XO.leng += 1
    
    def check(self):
        if self.contains(self.vis, [1,2,3]) or self.contains(self.vis, [4,5,6]) or self.contains(self.vis, [7,8,9]):
            XO.winner = self
        elif self.contains(self.vis, [1,4,7]) or self.contains(self.vis, [2,5,8]) or self.contains(self.vis, [3,6,9]):
            XO.winner = self
        elif self.contains(self.vis, [1,5,9]) or self.contains(self.vis, [3,5,7]):
            XO.winner = self
        
        return XO.winner
    
    def contains(self, arr, sub):
        if((set(arr) & set(sub)) == set(sub)):
            return True
        return False
    
    @staticmethod
    def printBoard():
        print("{}{}|{}|{} \t{}|{}|{}".format("\t"*2,XO.occupied[0],XO.occupied[1],XO.occupied[2],1,2,3))
        print("{}-+-+- \t-+-+-".format("\t"*2))
        print("{}{}|{}|{} \t{}|{}|{}".format("\t"*2, XO.occupied[3],XO.occupied[4],XO.occupied[5],4,5,6))
        print("{}-+-+- \t-+-+-".format("\t"*2))
        print("{}{}|{}|{} \t{}|{}|{}".format("\t"*2, XO.occupied[6],XO.occupied[7],XO.occupied[8],7,8,9))

if __name__ == '__main__':
    cls = lambda:os.system("cls")
    p1 = XO("X")
    p2 = XO("O")
    XO.printBoard()
    while not XO.winner and XO.leng != 9:
        p1.play()
        p1.check()
        cls()
        XO.printBoard()
        if not XO.winner and XO.leng != 9:
            p2.play()
            p2.check()
            cls()
            XO.printBoard()
    if XO.leng != 9:
        print("\n\tThe Winner is {}".format(XO.winner.name))
    else:
        print("\n\tMatch Tied")