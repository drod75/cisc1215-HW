a = "hello"
b = "world"
c = [1, 5, -4]
d = [21, 22, 23]
e = [9, 21, "c"]

print(sum(c + d))
print(list(b) * 2 + e)
print(b + str(e))
print(str(e) * 2 + b * 2)
print(a.split('e') + [str(c)])

print("!".join("1,2,3,4,3,2,1".split(",")))
print(",".join("1,2,3,4,3,2,1".split("2")))
print("1,2,3,4,3,2,1, ".split(','))