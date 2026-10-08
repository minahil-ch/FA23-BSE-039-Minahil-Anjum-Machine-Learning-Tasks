print("\n Lab Task 2: Factorial ")

n = int(input("Enter a number: "))

fact = 1  # factorial start 1 s
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial of", n, "is:", fact)