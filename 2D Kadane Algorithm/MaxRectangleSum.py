import sys
def kadane(givenNums):
    maxSum = -sys.maxsize-1
    currSum =0
    for num in givenNums:
        currSum = max(num,currSum+num)
        maxSum = max(maxSum,currSum)

    return maxSum

def maxRectangleSum(given2DArray):
    col = len(given2DArray[0])
    row = len(given2DArray)
    ans = -sys.maxsize-1

    for i in range(col):
        temp=[]
        for j in range(row):
            temp.append(given2DArray[j][i])
        ans = max(ans,kadane(temp))
        # print(temp)
        # print(ans)

        for j in range(i+1,col):
            for k in range(row):
                temp[k] += given2DArray[k][j]

            ans = max(ans,kadane(temp))


    return ans

matrix = [
    [3,8,9,1,3],
    [-4,-1,1,7,-6],
    [-2,-3,8,1,-1],
    [-2,-3,8,1,-1]
   
]

print(maxRectangleSum(matrix))