import re

s = input()

# s = re.sub('zero, one, two, three, four, five, six, seven, eight, nine', '[0-9]', s)
# while True:

answer = s.replace('zero', "0").replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')
answer = int(answer)
print(type(answer))

# if s == [0-9]:
#     print("")
# s = re.sub('[0-9]', 'X', s)
# a = s.replace('hello','hi')

print(answer)