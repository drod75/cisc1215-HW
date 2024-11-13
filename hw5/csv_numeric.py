def process_csv_numeric(data):
    nums = data.split(',')
    numerics = []
    for num in nums:
        numerics.append(float(num))
    return sum(numerics)

print(process_csv_numeric("1,2,3,4,5"))
print(process_csv_numeric("6,3,99,-21,4,31,2"))