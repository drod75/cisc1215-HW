omny_cap_rides = 34/2.90
print('{:.0f} rides are needed to reach cap'.format(omny_cap_rides))
last_fare = 34 - (2.90 * int(omny_cap_rides))
print('${:.2f} is the cost of the last ride'.format(last_fare))
