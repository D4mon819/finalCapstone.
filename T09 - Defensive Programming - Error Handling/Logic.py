
print("This is a Mathematics Power Calculator")
num_base = int(input("Number: "))
num_pow = int(input("Raised by the Power of: "))

result = num_base
for i in range(num_pow):
    result = result *num_base

print(f" {num_base} to the power of {num_pow} is {result}.")