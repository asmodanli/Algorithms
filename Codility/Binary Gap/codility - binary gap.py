import re

def solution(N):
    maxBinary = 0
    binaryN = bin(N).replace("0b", "")
    zeroList = re.findall("10+", binaryN)
    if binaryN[-1] == "0":
        del(zeroList[-1])
        zeroList.p
    for binNumber in zeroList:
        if len(binNumber) - 1 > maxBinary:
            maxBinary = len(binNumber)-1
    return maxBinary    

solution(32)