import re,traceback
import random
from collections import Counter 


class O:
    y=n=0
    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%"  % (
            O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc()) 
        return f
    
#1. Whitespace Formatting
def longWingedComputation():
    longWinged = (1+2+3+4+5)
    return longWinged


#2. Arithmetic
def divisionByTwo(x):
    return x/2

    
#3. Functions
def double(x):
    return 2*x

    
#4. Strings
def strings():
    string1 = 'akshay'
    string2 = "akshay"
    return string1 == string2


#5. Exceptions
def exceptions():
    try:
        return (0/0)
    except ZeroDivisionError:
        return ("Cannot divide by zero")
    
    
#6. Modules
def regex():
    result = re.search("a", "akshay")
    return result is not None


#7. Lists
def lists():
    return 27 in [27, 7, 94]
      

#8. Lists
def lenLists():
    return len([27, 7, 94])
    
    
#9. Tuples
def tuples_SumProduct(a, b):
    return (a+b),(a*b)

    
#10. Dictionaries
def dictionaries_getValue():
    details = {
        "first name" : "Akshay",
        "last name" : "Nalwaya",
        "university" : "NCSU"
    }
    return details.get("first name")


#11. dictionaries_checkKey
def dictionaries_checkValue():
    details = {
        "first name" : "Akshay",
        "last name" : "Nalwaya",
        "university" : "NCSU"
    }
    return "last name" in details
    
    
#12. dictionaries_Counter 
def dictionaries_counter():
    x = [2,7,0,7,1,9,9,4]
    counts = Counter(x)
    return counts.get(7) == 2


#13. Sets
def sets():
    mySet = set()
    mySet.add(2)
    mySet.add(7)
    mySet.add(7)
    return len(mySet)

    
#14. Control Flow
def control_flow(x):
    if(x % 2):
        return "Odd"
    else:
        return "Even"


#15. Truthfullness 1
def truthfullness():
    x = None
    return x is None

    
#16. Truthfullness 2
def truthfullness_all():
    x = [True, not False, 1==1]
    return all(x)

    
#17. Sorting
def sorting():
    x = [2,7,9,4]
    x.sort()
    return x


#18. List Comprehensions
def listComprehensions():
    x = [0,1,2,3,4]
    next_x = [i+1 for i in x]
    return next_x


#19. Generator
def generator():
    for i in [1,5]:
        yield i*2

    
#20. Randomness
def randomness(x):
    return random.choice(x)

    
#21. Regular expression
def regular_expression():
    search_result = re.search("c", "cat")
    return search_result is not None

    
class OOP_Set:
    def __init__(self, values=None):
        
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)
    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    #22. Object Oriented Programming - Add Function
    
    def add(self, value):
        self.dict[value] = True
    
    def contains(self, value):
        return value in self.dict

    #23. Object Oriented Programming - Remove Function    
    def remove(self, value):
        del self.dict[value]
    
    
#24. Functional tools
def exponent(a, b):
    return a**b

    
#25. Enumerate
def enum():
    details = {
        1 : 10,
        2 : 20,
        3 : 30}
    x = list()
    for i, _ in enumerate(details): x.append(i)
    
    return x

    
#26. Zip
def zipping(list1, list2):
    return zip(list1, list2)

    
#27. Argument Unpacking
def arg_unpack(a, b):
    return a*b



### Running unit tests  ###

@O.k
def testing_Whitespace():
    assert longWingedComputation() == 15


@O.k
def testing_divisionByTwo():
    assert divisionByTwo(7) == 3.5

@O.k
def testing_double():
    assert double(3) == 6

@O.k
def testing_strings():
    assert strings() == True

@O.k
def testing_exceptions():
    assert exceptions() == "Cannot divide by zero"

@O.k
def testing_regex():
    assert regex() == True

@O.k
def testing_lists():
    assert lists() == True
  
@O.k
def testing_lenLists():
    assert lenLists() == 3

@O.k
def testing_tuplesSumProduct():
    assert tuples_SumProduct(3,4) == (7,12)
    
@O.k
def testing_dictionariesGetValue():
    assert dictionaries_getValue() == "Akshay"

@O.k
def testing_dictionariesCheckValue():
    assert dictionaries_checkValue() == True

@O.k
def testing_dictionariesCounter():
    assert dictionaries_counter() == True

@O.k
def testing_sets():
    assert sets() == 2

@O.k
def testing_controlFlow():
    assert control_flow(7) == "Odd"
    
@O.k
def testing_truthfullness():
    assert truthfullness() == True

@O.k
def testing_truthfullnessAll():
    assert truthfullness_all() == True

@O.k
def testing_sorting():
    assert sorting() == [2,4,7,9]

@O.k
def testing_listComprehensions():
    assert listComprehensions() == [1,2,3,4,5]

@O.k
def testing_generator():
    genObj = generator()
    x = 0
    for i in genObj:
        x += i
    assert x == 12

@O.k
def testing_randomness():
    x = ["a", "b", "c"]
    assert randomness(x) in x

@O.k
def testing_regular_expression():
    assert regular_expression() == True

@O.k
def testing_oopAddFunction():
    newSet = OOP_Set([1,2,3,4])
    newSet.add(5)
    assert newSet.contains(5) == True

@O.k
def testing_oopDelFunction():
    newSet = OOP_Set([1,2,3,4])
    newSet.remove(3)
    assert newSet.contains(3) == False

@O.k
def testing_exponent():
    assert exponent(2,3) == 8
    
@O.k
def testing_enum():
    assert enum() == [0, 1, 2]

@O.k
def testing_zipping():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    newList = [(1, 'a'), (2, 'b'), (3, 'c')]
    assert list(zipping(list1, list2)) == newList

@O.k
def testing_arg_unpack():
    x = arg_unpack(*[5,10])
    assert x == 50



if __name__== "__main__":
  O.report()