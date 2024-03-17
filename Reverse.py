#Write a program that takes an integer as input and returns an integer with reversed digit ordering

def reverse_integer(num):
    reversed_num = 0
    is_negative = False  # Initialize a flag to indicate if the number is negative

    if num < 0:
        is_negative = True  # Set the flag to True if the number is negative
        num = abs(num)

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if is_negative:
        reversed_num *= -1  # Make the reversed number negative if the original number was negative

    return reversed_num

number = int(input("Enter a number: "))
reversed_number = reverse_integer(number)
print(reversed_number)
