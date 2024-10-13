def fine_calc(speed, speed_limit):
    fine = 0
    license_suspended = False
    if speed >= speed_limit + 10:
        fine += 50
    
    if speed > speed_limit + 10:
        extra_speed = speed - (speed_limit + 10)
        fine += (extra_speed * 5)


    if speed > 90 and speed <= 100:
        fine += 200
    if speed > 100:
        license_suspended = True
    return fine, license_suspended  
speed = float(input('Speed: '))
speed_limit = float(input('Speed Limit: '))
fs = fine_calc(speed, speed_limit)
print(f'Fine: ${fs[0]:.2f}')
if fs[1]:
    print('License is suspended')
else:
    print('License is active')