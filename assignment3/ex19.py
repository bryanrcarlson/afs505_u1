def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def my_function(input1, input2):
    my_string = f"{input1} is a {input2}"
    print(my_string)
    return my_string

my_function("bob", "man")
my_function("mallard", "duck")
my_function("four", "form of nothingness")
my_function(my_function("one", "number"), "string, actually")
#... and so on

def a_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3, sep = ", ")
var1 = 10
var2 = 20
a_function(var1, var2, var1 + var2)