#Write a program that takes an integer as input and returns true if the input is a power of two

def is_power_of_two():
    number = int(input("Enter a number: "))
    if number > 0 and (number & (number - 1)) == 0:
        print("True")
    else:
        print("False")

is_power_of_two()
