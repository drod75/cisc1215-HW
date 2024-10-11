num = int(float(input('Input a number to find all divisors: ')))
divisors = []
for x in range(1, num+1):
    if num % x == 0:
        divisors.append(x)
counter = 0
while counter != len(divisors) - 1:
    print(divisors[counter])
    counter += 1
if len(divisors) == 2:
    print('Prime Number')
else:
    print('Not a Prime Number')