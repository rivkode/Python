# n = 7
#
# for x in range(2, n):
#     if n % x == 0:
#         print(n, "equals", x ,"*", n//x)
#         break
# else:
#     print(n, "is a prime number")
#
# def factorial_for(n):
#     f = 1
#     for m in range(1, n+1):
#         f *= m
#     return f
#
# def factorial_rec(n=1):
#     if n <= 0:
#         return 1
#     else:
#         return n * factorial_rec(n-1)
# print(factorial_rec(10))
# print(factorial_for(10))
# print(factorial_rec())
# print(factorial_for())

# def mean_var(data):
#     n = len(data)
#     if n > 0:
#         mean = sum(data) / n
#         sum2 = sum([d**2 for d in data])
#         var = sum2 / n - mean**2
#         return mean, var
#     return None, None
#
# data = [3,2,9,1,0,8,7,5]
# pair = mean_var(data)
# mean, var = mean_var(data)
# mean, _ = mean_var(data)
# mean = mean_var(data)[0]
# print(mean)
# print(pair)
# print(var)

# from random import randint
#
# class Dice:
#     def throw(self):
#         return randint(1, 6)
# dice = Dice()
# print(dice.throw())
#
# from random import randint
#
# class Dice:
#     def __int__(self, boundary=(1, 6)):
#         self.start = min(boundary)
#         self.end = max(boundary)
#     def throw(self):
#         return randint(self.start, self.end)
#
# coin = Dice((0, 1))
# print(coin.throw())
#
# dice = Dice()
# print(dice.throw())

# prof_dict = {'name':'choi', 'room_no':327, 2021:True}
#
# a = 'my name is %s and my room is %d' %('choi', 327)
# print(a)
# b = 'my name is %(name)s and my room is %(room_no)04d' %prof_dict
# print(b)
#
# c = 'my name is {} and my room is {}'.format('choi', 327)
# print(c)
# d = 'my name is {1} and my room is {0}'.format(327, 'choi')
# print(d)
#
# e = 'my name is {name} and my room is {room_no:04d}'.format(**prof_dict)
# print(e)

# data = [3, 2, 9]

# a = data.sort()
# b = data.sort(reverse = True)
# c = data.sort(key=lambda x: abs(x-9))
# print(data)

# pts =[(3, 29), (10, 18), (10, 27), (5, 12)]
#
# nearest_pts = sorted(pts, key=lambda pt: pt[0]**2 + pt[1]**2)
# print(nearest_pts)

# squares = [] #c 스러운 스타일 코드
# for x in range(10):
#     squares.append(x**2)
# print(squares)

#squares = list(map(lambda x:(x**2), range(10)))
#print(squares)

# squares = [x**2 for x in range(10)] #list comprehension
# print(squares)

