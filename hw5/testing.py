a = "hello"
b = "world"
c = [1, 5, -4]
d = [21, 22, 23]
e = [9, 21, "c"]
b2 = [10, 60, 31, -22, 14, 49, 31, -100, -200, 369]

print(sum(c + d))
print(list(b) * 2 + e)
print(b + str(e))
print(str(e) * 2 + b * 2)
print(a.split('e') + [str(c)])

print("!".join("1,2,3,4,3,2,1".split(",")))
print(",".join("1,2,3,4,3,2,1".split("2")))
print("1,2,3,4,3,2,1, ".split(','))

print(b2[-8:8])