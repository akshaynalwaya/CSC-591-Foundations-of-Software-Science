import re,traceback

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


DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""


DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""


#Function to parse lines and remove lines with nothing
def lines(s):
    result = []
    splittedLines = s.splitlines()
    for lines in splittedLines:
        if(lines):
            result.append(lines.strip())
    
    return result   


def rows(src):
    
    formattedRows = ""
    for line in src:
        line = re.sub(r"\s+","",line)
        if '#' in line:
            line = line.split('#')[0]
        formattedRows += line
        if not line.endswith(","):
            formattedRows += "\n"
        
    return formattedRows.splitlines() 
    

#ignore columns with '?' 
def cols(src):
    newCols = []
    topRow = src[0].split(',')
    pos = -1
    for name in topRow:
        if(name[0] == '?'):
            pos = topRow.index(name)

    topRow.pop(pos)
    newCols.append(topRow)

    for s in src[1:]:
        colValues = s.split(',')
        colValues.pop(pos)
        newCols.append(colValues)

    return newCols

#Converting the string values into float for a column
def prep(src):
    preppedData = []
    pos = -1
    for name in src[0]:
        if(name[0] == '$'):
            pos = src[0].index(name)
    
    for s in src[1:]:
        s[pos] = float(s[pos])
    
    return src

    
    
#---------------TESTING FUNCTIONS-------------#
def ok0(s):
    for row in prep(cols(rows(lines(s)))):
        print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

