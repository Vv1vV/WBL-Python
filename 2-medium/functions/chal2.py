def multiCheck(inA, inB, inC=2):
    outA = inA * inB
    if outA % inC == 0:
        return True
    else:
        return False


def plusArr(inA, inB):
    outA = inA + inB
    arr = []

    for i in range(outA+1):
        arr.append(i)
    return arr
