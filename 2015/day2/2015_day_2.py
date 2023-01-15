f = open('day2/input.txt')


def partOne():
    totalPaper = 0
    for line in f:
        l,w,h =  line.split("x")
        lengteLW = int(l)*int(w)
        lengteWH = int(w)*int(h)
        lengteLH = int(l)*int(h)
        minimal = min(lengteLH,lengteLW, lengteWH)
        totalPaper += (2*lengteLW + 2*lengteWH + 2*lengteLH + minimal)

    print(totalPaper)

def parttwo():
    totalPaper = 0
    for line in f:
        l,w,h =  line.split("x")
        lengteLW = int(l)+int(w)+int(l)+int(w)
        lengteWH = int(w)+int(h)+int(w)+int(h)
        lengteLH = int(l)+int(h)+int(l)+int(h)
        feet = min(lengteLH,lengteLW, lengteWH)
        totalPaper += (int(l) * int(w) * int(h) + feet)
    print(totalPaper) 

parttwo()
