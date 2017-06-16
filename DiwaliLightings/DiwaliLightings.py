
testCases = []
casenum = 1

def readIn(f):
    cases = int(f.readline())
    for i in range(cases):
        lights = f.readline().strip()
        vals = f.readline().split()
        vals = [int(v) for v in vals]
        testCases.append((lights,vals[0], vals[1]))
        
def countBlue(lights, startPosn = 0, endPosn = -1):
    if endPosn == -1:
        endPosn = len(lights)
    return lights.count("B", startPosn, endPosn)

def countLeadingLights(lights,i):
    # Number of lights before the first full pattern 
    startPosn = (i-1) % len(lights)
    if startPosn == 0:
        return 0
    return len(lights[startPosn:])

def countTrailingLights(lights,i):
    # Number of lights after the completion of full patterns
    return i % len(lights)

def calcBlueLights(lights, i, j):
    # Initial implementation basically tried to cut things into 3 sections: stuff before full patterns (leading), full patterns, and stuff after (trailing).
    # Unfortunately, calculating the middle portion basically required all the important info from the other two sections.
    # This is a minutely improved version based on an odd observation: you can combine leading and trailing and almost get a full pattern.  
    
    leading = countLeadingLights(lights,i)
    trailing = countTrailingLights(lights,j)
    
    leadingIx = len(lights) - leading # What index they actually start on
    
    # Brackets are important.
    blueLights = countBlue(lights) * ((j-i+1) // len(lights))
    
    if trailing > leadingIx:
        # The trailing lights overlap with the leading ones, we'll need to double count the overlap.
        blueLights += countBlue(lights, leadingIx, trailing)
    elif trailing < leadingIx:
        # The trailing lights are disjoint with the leading ones and we'll need to count more since they didn't form a full extra pattern.
        # 0 leading lights will also go here (where it's also correct)
        blueLights += countBlue(lights) - countBlue(lights, trailing, leadingIx)
    else:
        # The trailing and leading lights form exactly another group! (we already accounted for that, so do nothing)
        pass
    outline = 'Case #%d: %d\n' % (casenum, blueLights)        
    outFile.write(outline)
    print(outline)
        
f = open('A-large-practice.in')
readIn(f)
outFile = open('diwalilightingslarge.out','w')

for c in testCases:
    calcBlueLights(c[0],c[1],c[2])
    casenum += 1