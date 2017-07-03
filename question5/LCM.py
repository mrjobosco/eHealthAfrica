def greatestCommonFactorForTwo(a, b):
    if b == 0:
        return a
    else:
        return greatestCommonFactorForTwo(b, (a%b))


def greatestCommonFactorForN(arr = []):
    number = arr[0]
    for i in range(len(arr)):
        number = greatestCommonFactorForTwo(number, i)
    return number


def lcmForTwo(a, b):
    return (a * b)/greatestCommonFactorForTwo(a,b)

def lcm(arr):
    number = arr[0]
    for i in arr:
        number = lcmForTwo(number, i)
    return number




print(lcm([2,3,4,5,6]))
