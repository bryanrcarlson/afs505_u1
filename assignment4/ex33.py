#i = 0
#numbers = []
#
#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")
#
#
#print("The numbers: ")
#
#for num in numbers:
#    print(num)



def number_game(max_value, step_size):
    i = 0
    numbers = []

    while i < max_value:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step_size
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

def number_game2(max_value, step_size):
    numbers = []
    for i in range(0, max_value, step_size):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

number_game(3, 0.5)
number_game(8, 2)
number_game2(8, 2)