

def square3(cnt):
    if cnt == 0:
        return

    for i in range(1, 1+cnt):
        print("*"*cnt)
        if i%2==0:
            print(("*"+" "+"*")*(cnt//3))
    cnt -=1
    square3(cnt)
square3(27)
