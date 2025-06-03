#1
print("First exercise")
greetings_to_Python = "Hello, Python World!"
print(greetings_to_Python)
#2
print("\nSecond exercise")
x = int(input("Write the number #1\n"))
y = int(input("Write the number #2\n"))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
#3
print("\nThird exercise")
first_row = "Привіт, "
second_row = input("Як тебе звати?\n")
print(first_row + second_row)
print("Quantity of characters in this expression: ", len(first_row + second_row))
#4
print("\nFourth exercise")
number = int(input("Write any number\n"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#5
print("\nFifth exercise")
for i in range (1, 11):
    print(i)
#6
print("\nSixth exercise")
number = int(input("Write any number\n"))
if number > 0:
    print("Posiive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
#7
print("\nSeventh exercise")
for i in range (1, 11):
    if i % 2 == 0:
        print(i)
#8
print("\nEighth exercise")
number = int(input("Write any number\n"))
nothing = []
for i in range (1, number + 1):
    nothing.append(i)
print(sum(nothing))
#9
print("\nNinth exercise")
for i in range (10, 0, -1):
    print(i)
#10
print("\nTenth exercise")
for i in range (1, 11):
    if i == 5:
        continue
    elif i == 7:
        break
    print(i)