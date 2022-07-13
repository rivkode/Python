# while True:
#     if b > a:
#         a, b = b, a
#
#     share = a // b
#     remainder = a % b
#     # a = b*share + remainder
#     # b = remainder*share + remainder1
#     if remainder == 0:
#         break
#     else:
#         b // remainder

def gcd(a, b):
    if b > a:
        a, b = b, a
    tmp = a % b
    if tmp == 0:
        return


    gcd(b, tmp)

a, b = map(int, input().split())

