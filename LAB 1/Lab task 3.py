print("\n Lab Task 3: Fibonacci Series ")

terms = int(input("Enter how many terms you want: "))

a = 0  # 1st number
b = 1  # 2nd number
i = 0

print("Fibonacci Series:")

while i < terms:
    print(a, end=" ")  
    c = a + b          # next number
    a = b              # a ko b bana do
    b = c              # b ko c bana do
    i = i + 1