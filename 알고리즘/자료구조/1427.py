import sys
input = sys.stdin.readline

InputNum = int(input())
StrInputNum = str(InputNum)

numLst = []
numberLen = len(StrInputNum)

for i in range(numberLen):
    numLst.append(int(StrInputNum[i]))

for i in range(numberLen):
    if numLst[i] < numLst[i+1]:
        tmp = numLst[i]
        numLst[i] = numLst[i+1]
        numLst[i+1] = tmp

print(numLst)

def swap(numLst):
    tmp = numLst[i]
    numLst[i] = numLst[i + 1]
    numLst[i + 1] = tmp


