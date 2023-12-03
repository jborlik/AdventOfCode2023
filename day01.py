#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


CNUMINTS = ['0','1','2','3','4','5','6','7','8','9']
#CREVNUMINTS = [reversed(s) for s in ]
CNUMWORDS = ['zero','one','two','three','four','five', 'six', 'seven', 'eight','nine']
CNUMWORDS.extend(CNUMINTS)
CREVNUMWORDS = [s[::-1] for s in CNUMWORDS]

with open('day01.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()]   # 

testdata2 = [x.strip() for x in """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()]


#thedata = testdata2
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if False:

    START = time.perf_counter()

    totval = 0
    for aline in thedata:

        #firstdig = next((x for x in CNUMINTS if x in aline), False)        
        #lastdig = next((x for x in CNUMINTS if x in aline[::-1]), False) 
        firstdig = next((x for x in aline if x in CNUMINTS), False)        
        lastdig = next((x for x in aline[::-1] if x in CNUMINTS), False) 
        val = int(f"{firstdig}{lastdig}")
        print(val)
        totval += val
    
    print(f"FIRST:  total value = {totval}")




    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

totval = 0
for aline in thedata:

    #firstdig = next((x for x in CNUMINTS if x in aline), False)        
    #lastdig = next((x for x in CNUMINTS if x in aline[::-1]), False) 
    firstdig = 0
    for i in range(len(aline)):
        if firstdig != 0:
            break
        for ival,aword in enumerate(CNUMWORDS):
            if aline[i:].startswith(aword):
                if ival > 10:
                    ival -= 10
                print(f"FOUND! {aword}, {ival}")
                firstdig = ival
                break

    secondig = 0
    for i in range(len(aline)):
        if secondig != 0:
            break
        for ival,aword in enumerate(CREVNUMWORDS):
            revline = aline[::-1]
            if revline[i:].startswith(aword):
                if ival > 10:
                    ival -= 10
                print(f"FOUNDREV {aword}, {ival}")
                secondig = ival
                break

    theval = firstdig * 10 + secondig
    print(theval)
    totval += theval
    
print(f"SECOND:  total value = {totval}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")