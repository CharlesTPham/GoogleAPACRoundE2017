import math

testCases = []
casenum = 1


def poly(x,d):
    # x^d + x^d-1 + x^d-2 + ... + x
    return sum([x**k for k in range(1,d+1)])

def dPoly(x,d):
    # Derivative of the above polynomial
    return sum([k*x**(k-1) for k in range(1,d+1)])

def newtonsMethod(f, df, x0):
    prev = x0 + 100
    while abs(prev-x0) > 1: # Possibly unsafe? (I can't imagine it'd be considering it SHOULD be pretty much a straight line?)
        prev = x0
        x0 = x0 - f(x0)/df(x0)
    return round(x0)

def readIn(f):
    cases = int(f.readline())
    for i in range(cases):
        testCases.append(int(f.readline()))
    
solutions = {}
def populateSolutions():
    # The brute force method: build everything. 1k is a pretty small number so this can be done trivially.
    for b in range(2,1001):
        accum = 1
        x = 1
        accum += b**x
        while (accum <= 1000):
            if (accum not in solutions):
                solutions[accum] = b
            x += 1
            accum += b**x  

def trivialProcessCase(c):
    # Solution used for smaller version
    if c in solutions:
        sol = solutions[c]
    else:
        sol = c-1
    outline = 'Case #%d: %d\n' % (casenum, sol)        
    outFile.write(outline)
    print(outline)
    
def tryToBuildUp(c, b):
    # Try to build up c using sums of base b
    # Maybe numerical error so try to account for that?
    for guess in range(max(2,b-10), b+10):
        accum = 1
        x = 1
        accum += guess**x
        while (accum < c):
            x += 1
            accum += guess**x
        if accum == c:
            return guess
    return -1
    

def processCase(c):
    # Try to find the smallest integer soln to x^k + x^k-1 + ... + x - c

    for i in reversed(range(2,60)): # 2^60 exceeds the upper bound of what we're looking for, start with larger exponents since they generate more 1s
        guess = math.log(c,i) # approximate the as x^i
        betterguess = newtonsMethod(lambda x: poly(x,i)-c, lambda x: dPoly(x,i), guess) # get a better guess with newton's method
        if betterguess < 0:
            print("**************how is this even possible?")
        rv = tryToBuildUp(c,int(betterguess))
        if rv > 0:
            print('***** %d is %d to the %d' %(c, rv, i))
            result = rv
            break
    else:
        print('could not find way to print %d' % c)
        # You can always write a number as 
        result = c - 1
    
    outline = 'Case #%d: %d\n' % (casenum, result)        
    outFile.write(outline)
    print(outline)
    
f = open('B-large-practice.in')
readIn(f)
outFile = open('beautifulnumberlarge.out','w')
    
#populateSolutions()
    
for c in testCases:
    #trivialProcessCase(c)
    processCase(c)
    casenum += 1
