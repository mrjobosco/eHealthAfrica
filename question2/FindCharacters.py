def find_chars_OrderNN(string1, string2):
    str = []
    for c in string1:
        if c in string2:
            str.append(c)

    return ''.join(str)



def find_chars_OrderN(string1, string2):
    str = []
    setOfString2 = set(string2)
    for c in string1:
        if c in setOfString2:
            str.append(c)

    return ''.join(str)






