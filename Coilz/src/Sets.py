print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print('intersection')
print(a.intersection(b))
print(b.intersection(a))

print('issubset')
print(a.issubset(b))
print(b.issubset(a))

print('symmetric_difference')
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print('difference')
print(a.difference(b))
print(b.difference(a))

print('union')
print(a.union(b))
