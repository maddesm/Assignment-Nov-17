# Part2: hackerrank
# first : if three sides can form a non-degenerate triangle 
# then maximum Perimeter Triangle 
# PAY ATTENTION Check if these sides form a triangle

import os

def is_valid(a, b, c):
    return a + b > c

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True) 
 # put them in ascendeing
    for i in range(len(sticks) - 2):
        a, b, c = sticks[i], sticks[i+1], sticks[i+2]
        if is_valid(b, c, a): 
            return [c, b, a] 
    
    return [-1]  
#if there's no triangle 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    sticks = list(map(int, input().strip().split()))

    result = maximumPerimeterTriangle(sticks)
    fptr.write(' '.join(map(str, result)) + '\n')
    fptr.close()

# Status: Accepted 