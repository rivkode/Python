import sys

N = int(sys.stdin.readline())
INPUT_LST = sys.stdin.readline().split()
lst = list(map(int, INPUT_LST))

MAX_NUMBER = max(lst) # 가장 큰수 찾기
MAX_INDEX = lst.index(MAX_NUMBER) # 가장 큰수 인덱스
del lst[MAX_INDEX] # 가장 큰수 제거
LST_LEN = len(lst) # 리스트 원소 개수

LST_SUM = sum(lst)
MAX_SUM = MAX_NUMBER*LST_LEN

RESULT = LST_SUM + MAX_SUM

print(RESULT)