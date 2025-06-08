#Початковий рівень
#1
print("Beginner level\n1 exercise")
my_list = [1,2,3,4,5,6,7,8,9,10,13,27,222]
print(sum(my_list))

#2
print("\n2 exercise")
print(min(my_list))

#3
print("\n3 exercise")
reversed_list = my_list[::-1]
print(reversed_list)

#4
print("\n4 exercise")
for i in my_list:
    if i % 2 == 1:
        print(i, end= " ")

#5
print("\n\n5 exercise")
for i in my_list:
    print(i*2, end=" ")

#Легкий рівень
#1

print("\n\nEasy level\n1 exercise")
for i in my_list:
    if i > 3:
        print(i, end= " ")

#2
print("\n\n2 exercise")
sum_of_my_list = sum(my_list)
len_of_my_list = len(my_list)
print(sum_of_my_list / len_of_my_list)

#3
print("\n3 exercise")
blank_list_0 = []
for i in my_list:
    if i < 8:
        blank_list_0.append(i)
maximum_of_new_list = max(blank_list_0)
print(maximum_of_new_list)

#4
print("\n4 exercise")
blank_list_1 = []
for i in my_list:
    if i % 2 == 0:
        blank_list_1.append(i)
print(sum(blank_list_1))

#5
print("\n5 exercise")
blank_list_2 = []
for i in my_list:
    squared = i ** 2
    blank_list_2.append(squared)
print(*blank_list_2)

#6
print("\n6 exercise")
blank_list_3 = []
for i in my_list:
    if i > 0 == 0:
        blank_list_3.append(i)
print(*blank_list_3)

#7
print("\n7 exercise")
blank_list_5 = []
for i in my_list:
    num_as_string = str(i)
    if str(i).startswith("2"):
        print(i)

#8
print("\n8 exercise")
input_of_user = int(input("Write the n numbers you want to add from my_list\n"))
try:
    if input_of_user < len(my_list):
        print(sum(my_list[:input_of_user]))
    elif input_of_user >= len(my_list):
        print(sum(my_list))
except ValueError:
    print("Write a number (integer perfectly), not anything else")

#9
#palindrom - is a number that we can read from on side to another and vice versa without losing its meaning. For instance 1221 or 23232
print("\n9 exercise")
for i in my_list:
    if isinstance(i, str):
        palindrom = i[::-1]
        if i == palindrom:
            print(i)
    else:
        print(f"Element {i} is not a string")
#10
print("\n10 exercise")
input_of_user_2 = int(input("Write the number you want to divide all numbers and I will show you the numbers without ramainder\n"))
blank_list_4 = []
try:
    for i in my_list:
        if i % input_of_user_2 == 0:
            blank_list_4.append(i)
    print(*blank_list_4)
except ValueError:
    print("Write a number (integer perfectly), not anything else")

#Medium level
#1
print("\nMedium level\n1 exercise")
for i in my_list:
    if i % 2 == 0 and i % 4 != 0:
        print(i, end= " ")

#2
print("\n\n2 exercise")
my_list_1 = [1,2,3,4,5,6]
my_list_2 = [7,8,9,10,13,27,222]
my_list_3 = my_list_1 + my_list_2
print(my_list_3)

#3
print("\n3 exercise")
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
my_list_4 = ["Apple", "Orange", "Banana", "Marakuya", "hello"]
for i in my_list_4:
    if i[0] in capital_letters:
        print(i[0])

#4 (на жаль без сортування за кількістю кожного числа, бо я не зумів здогадатися як це зробити)
print("\n4 exercise")
my_list_5 = [1,2,3,4,4,5,6,6,6,7,8,9,10,10,10,10]
reversed_list_5 = sorted(my_list_5, reverse=True)
print(reversed_list_5)

#5
print("\n5 exercise")
my_list_11 = [1,2,3,4,5,6]
my_list_22 = [7,8,9,10,13,27,222]
my_list_33 = my_list_11[1:4] + my_list_22[1:4]
print(my_list_33)

#6
print("\n6 exercise")
dict_1 = {
    "ones": [1,2,3],
    "tens": [10,11,12],
    "hundreds": [100,101,102]
}
sum_of_tens = sum(dict_1["tens"])
print(sum_of_tens)

#7
print("\n7 exercise")
my_list_7 = [7,8,9,10,13,27,222]
for i in range(len(my_list_7)):
    if my_list_7[i] % 3 == 0:
        my_list_7[i] = 3
print(my_list_7)

#8
print("\n8 exercise")
my_list_8 = ["Apple", "Football", "Game", "Politologist"]
for i in my_list_8:
    length_of_string = len(i)
    if length_of_string > 6:
        print(i)

#9
print("\n9 exercise")
my_list_8 = ["Apple", "Football", "Game", "Politologist"]
my_list_9 = ["Orange", "Basketball", "Rocky", "Historist"]
print(my_list_8[0], my_list_9[0], my_list_8[1], my_list_9[1], my_list_8[2], my_list_9[2], my_list_8[3], my_list_9[3])

#10
print("\n10 exercise")
my_list = [1,2,3,4,5,6,7,8,9,10,13,27,222]
for i in my_list:
    if i > 5:
        print(i*0.5)
    
print("That is over!")