import sys
def flip(bit):
    if bit =="0":
        return 1
    else:
        return -1

def getMaximumFlipBits(givenBits):
    ans =0
    for bit in givenBits:
        if bit =="1":
            ans +=1

    maxSum =-sys.maxsize-1
    currSum =0
    start = 0
    end =0
    n = len(givenBits)
    while end<n:
        while currSum<0:
            currSum -= flip(givenBits[start])
            start +=1
        currSum += flip(givenBits[end])
        end +=1
        maxSum = max(maxSum,currSum)
    return ans + maxSum

bits ="0001000"
print(getMaximumFlipBits(bits))