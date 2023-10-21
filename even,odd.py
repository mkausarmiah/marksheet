

a = int(input('Enter the start number: '))
b = int(input('Enter the end number: '))

#For even number list
print("Even numbers list...")
for k in range(a, b + 1):
    if k % 2 == 0:
        print(k)

#For odd number list
print("Odd numbers list...")
for k in range(a, b):
    if k % 2 != 0:
        print(k)

