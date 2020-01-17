# Kind of like a template for a string
formatter = "{} {} {} {}"

# Prints various versions of the template, injecting respective variables into their respective {} (what's that called?), by sequence, using the "format" function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Tricky, nested formatter!
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

print(formatter.format(
    "Does one",
    "tab",
    "or space",
    "in the world of Python?"
))