# while True:
#     s = list(map(str, input()))
#     if s == ["."]:
#         break
#     for i in range(len(s)):
#         cnt1 = 0
#         cnt2 = 0
#
#         result1 = 0
#         result2 = 0
#
#         for j in s:
#             if j == "(":
#                 cnt1 +=1
#             elif j == ")":
#                 cnt1 -=1
#                 if cnt1 < 0:
#                     result1 = "no"
#                     break
#                 else:
#                     continue
#             elif j == "[":
#                 cnt2 +=1
#             elif j == "]":
#                 cnt2 -=1
#                 if cnt2 < 0:
#                     result2 = "no"
#                     break
#                 else:
#                     continue
#         if result1 or result2 == "no":
#             print("no")
#             break
#         else:
#             print("yes")
#             break

while True:
    s = input() # input 도 for 문을 사용하면 list처럼 문자열 하나씩 읽어들일 수 있다
    stack = []
    if s == ".":
        break
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) !=0 and stack[-1] == '[':
                stack.pop() #이전과 비교해서 동일하면 stack을 비워줌# 맞으면 지워서 stack을 비워줌 0 = yes
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
