n = int(input())
str_lst = list(input())
# print(str_lst)
#lst = {"a":1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
num_lst = []


for i in range(n):
    # num_lst.append(lst[str_lst[i]]*(31 ** (lst[str_lst[i]]-1)))
    num_lst.append((ord(str_lst[i]) - 96) * (31 ** i))

sum = sum(num_lst)
print(sum%1234567891)
