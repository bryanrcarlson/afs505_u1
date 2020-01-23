from sys import argv

script, filename = argv

print(f"We're... {filename}.")
print("If...")
print("If...")

input("?")

print("Opening...")
target = open(filename, 'w')

print("Trun..")
target.truncate()

print("Now...")

line1 = input("1: ")
line2 = input("2: ")
line3 = input("3: ")

print("I'm...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

print("Now we'll read it")

myfile = open(filename, 'r')
print(myfile.read())
myfile.close()
