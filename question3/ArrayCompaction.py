def arrayCompaction(arr=[]):
    number = arr[0]
    duplicate = False
    new_arr = []

    for i in arr:

        if number == i and duplicate == False:
            duplicate = True
        elif number != i:
            new_arr.append(number)
            number = i
            duplicate = False
    new_arr.append(arr[len(arr) - 1])
    return new_arr
