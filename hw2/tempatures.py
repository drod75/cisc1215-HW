total = int(input("How many temperatures do you want to convert? "))
for x in range(total):
    celsius = float(input('Temperature (C): '))
    fahrenheit = celsius * 9 / 5 + 32
    print('F: {:.2f}'.format(fahrenheit))