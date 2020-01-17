# instantiats variable named "cars" and assigns the int value 100 to it
cars = 100
# instantiates variable named "space_in_a_car" and assigns float value of 4.0 to it
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

# Study Drills
# 0) Extra underscore in "carpool"
# 1) Float to Int -- saves memory but lose precision