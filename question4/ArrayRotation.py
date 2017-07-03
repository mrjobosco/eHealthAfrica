def getNewArray(arr, i, number):
    arr[i] = number
    return arr


def rotateArray(arr, N):

    for i in range(N):
        lastNumber = arr[-1]
        for j in range(len(arr)- 2, -1, -1):
            moveNumber = arr[j]
            arr = getNewArray(arr, j+1, moveNumber)
        arr[0] = lastNumber

    return arr





