import math, re, traceback
from sample import Sample
from num import Num
from sym import Sym
from random import random
from random import seed

class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


@O.k
def testing_Sample():
    seed(1)
    s = list()

    for i in range(5,11):
        s.append(Sample(2**i))

    for i in range(1,10001):
        y = random()
        for t in s:
            t.sampleInc(y)

    for t in s: 
        print(t.max_val,t.nth(0.5))
        low = .05 - .33
        hi = 0.5 + .33
        assert ((t.nth(0.5) >= low) and (t.nth(0.5) <= hi))


@O.k
def testing_Sym():
    s1 = Sym()
    s1 = s1.syms([ 'y','y','y','y','y','y','y','y','y','n','n','n','n','n'])
    print(s1.symEnt())
    result = round(s1.symEnt(),4)
    assert (result == 0.9403)


@O.k
def testing_Num():
    n1 = Num()
    n1 = n1.nums([4,10,15,38,54,57,62,83,100,100,174,190,215,225,233,250,260,270,299,300,306,333,350,375,443,475,525,583,780,1000])

    print(n1.mu, n1.sd)
    assert(n1.mu == 270.3)
    result = round(n1.sd,3)
    assert(result == 231.946)
    

if __name__== "__main__":
  O.report()
