def fine_calc(speed, speed_limit):
    pass

speed = float(input('Speed: '))
speed_limit = float(input('Speed Limit: '))
fs = fine_calc(speed, speed_limit)
print(f'Fine: ${fs[0]}')
if fs[1]:
    print('License is suspended')
else:
    print('License is active')