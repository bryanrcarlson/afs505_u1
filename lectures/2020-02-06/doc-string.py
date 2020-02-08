def square(a):
    '''Returns arg a is squared.'''
    return a**a

#print(square.__doc__)

def some_funct(arg1):
    """ summary

    parameters:
    arg (int): desc

    Returns:
    int: returning
    """
    return arg1

# print(some_funct.__doc__)

# Standards: PyDoc + Sphinx: generates website for documentation

# Always do this, ensures no globals and allows script to be imported:
def main():
    print("Hello")

if __name__ == "__main__":
    main()

