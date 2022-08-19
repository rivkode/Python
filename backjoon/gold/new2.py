a = [[1, 2], [3, 4], [5, 6]]
b = a[:]

print(f"id(a) = {id(a)}\nid(b) = {id(b)}")
print(f"a = {a}\nb = {b}")

print("=========================")

print(f"id(a[0]) = {id(a[0])}\nid(b[0]) = {id(b[0])}")
print(f"a[0] = {a[0]}\nb[0] = {b[0]}") #deepcopy라는데 나중에 공부해보도록 하자