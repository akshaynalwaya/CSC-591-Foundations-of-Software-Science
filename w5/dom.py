from num import Num
from sym import Sym
from rows import Rows, rows
from test import O
import re, sys, random, math

def another(r, rows):
    ar = math.floor(0.5 + random.random()*len(rows))
    if not r == ar:
        return rows[ar]
    return another(r, rows)

def dom(t, row1, row2):
    s1 = 0
    s2 = 0
    n = len(t.w)
    for c, w in t.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = t.nums[c].numNorm(a0)
        b = t.nums[c].numNorm(b0)
        s1 = s1 - Math.pow(10,(w * (a-b)/n))
        s2 = s2 - Math.pow(10,(w * (b-a)/n))
    return s1/n < s2/n

def doms(t):
    #assuming the number of samples as 100
    n = 100
    c = len(t.name)
    print("\t".join(t.name)+"\t>dom")
    for r1, row1 in enumerate(t.rows):
        row1.append(0)
        for i in range(1,n):
            row2 = another(r1, t.rows)
            s = dom(t, row1, row2) and 1/n or 0
            row1[c] = row1[c] + s
    
    for row in t.rows:
        row[len(row)-1] = str("%.2f"%row[len(row)-1])
        print("\t".join(str(r) for r in row))


def mainDom(csv):
    doms(rows(csv))

@O.k
def test():
    print("\nweatherLong.csv\n")
    mainDom("weatherLong.csv")

    print("\nauto.csv\n")
    mainDom("auto.csv")

