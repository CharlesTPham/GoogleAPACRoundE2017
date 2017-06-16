testCases = []
casenum = 1

def findRemainder(n, d, b):
    # Everyone bucket needs at least x*d balls
    baseNum = n / (d * b)
    remaining = n % (d * b)
    if (remaining > 2 * (b-1) or remaining == n):
        return -1
    else:
        return remaining

def canLeech(r,d,b,n):
    # Can we put d from all buckets into the remainder and still make partitions?
    if (r + d*b) > (2 *(b-1)):
        # Can't remove because that leaves remainder too large
        return False
    if (b > n/d/2):
        # Can't remove since leftmost bucket has only 1 in it
        return False
    return True

def numberOfWaysToArrangeRemainder(r, b):
    # Given r balls remaining, find all valid ways to put them into b buckets
    # Basically, cram all the balls to the right (r/2) buckets,
    # then you generate all arrangements by chipping off the top layer of a doubled up bucket and putting into an empty bucket.
    
    if (r > 2*(b-1)):
        print("Impossibly large remainder?")
    if (r < 0):
        print("Impossibly small remainder?")
    
    # The number of possible times we can chipping off the top
    chipNumber = int(r/2)
    
    # The number of empty buckets we can put chipped balls into
    freeNumber = b - int(r/2) - (r%2) - 1
    
    # If there's not enough free buckets to chip into, you're limited by that.
    rv = min(chipNumber, freeNumber)
    
    # The original arrangement is also valid
    rv += 1

    return rv
    
def processCase(c):
    n = c[0]
    d = c[1]
    
    print("Prob n = %d d = %d" % (n,d))
    
    accum = 0
    for b in range(1,n+1):
        remainder = findRemainder(n,d,b)
        if remainder > -1:
            accum += numberOfWaysToArrangeRemainder(remainder, b)
            if canLeech(remainder, d, b, n):
                accum += numberOfWaysToArrangeRemainder(remainder + b, b) 
        elif (d == 1):
            accum += numberOfWaysToArrangeRemainder(remainder-b, b)
    
    outline = 'Case #%d: %d\n' % (casenum, accum)        
    outFile.write(outline)
    print(outline) 

def readIn(f):
    cases = int(f.readline())
    for i in range(cases):
        testcase = f.readline().split()
        testcase = [int(c) for c in testcase]
        testCases.append(testcase)
        
    
f = open('C-large-practice.in')
readIn(f)
outFile = open('partitioningnumberlarge.out','w')

for c in testCases:
    processCase(c)
    casenum += 1

    