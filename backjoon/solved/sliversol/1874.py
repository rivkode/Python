n = int(input())
stack = []
result = []
no_answer = True
count = 0

for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        result.append("+")
        stack.append(count)

    if x == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        no_answer = False
        break


if no_answer == False:
    print("NO")
else:
    print("\n".join(result))

