# Display countdown from 20 to 0
countdown = 20
print("Countdown from 20 to 0:")
while countdown >= 0:
    print(countdown)
    countdown -= 1
# Display even numbers between 1 and 20
print("Even numbers between 1 and 20:")
for i in range(1, 21):
    if i % 2 == 0:                      # If a number divided by two and have no remainder, it's a even number
        print(i)
# Display the star pattern
for i in range(1, 6):
    star = "*" * i
    print(star)
