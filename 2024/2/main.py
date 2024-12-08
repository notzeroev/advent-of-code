import copy

input = open("input.txt", "r")
safeCount = 0
lines = input.readlines()

def CheckSafe(arr):

    isNeg = arr[1] - arr[0] < 0

    for i in range(len(arr) - 1):
        step = arr[i + 1] - arr[i]

        if(isNeg):         
            if(step > -1 or step < -3):
                return False
        else:
            if(step < 1 or step > 3):
                return False
            
        
    return True

def loopCheck(checkArr):
    for i in range(len(checkArr)):
            temp = copy.deepcopy(checkArr)
            temp.pop(i)

            if(CheckSafe(temp)):
                return True
    return False


for line in lines:
    numbers = list(map(int, line.split()))

    if(CheckSafe(numbers)):
        print(f"safe: {numbers}")
        safeCount += 1
    else:
        if(loopCheck(numbers)):
            print(f"safe: {numbers}")
            safeCount += 1
        

print(safeCount)


