n = int(input("Enter the range for powers of 2: "))

powers_of_2 = map(lambda x: 2 ** x, range(n + 1))

print("Powers of 2:")
for power in powers_of_2:
    print(power)

