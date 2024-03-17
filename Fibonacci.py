#Write a program to generate the Fibonacci sequence up to 100

def generate_fibonacci_sequence():
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= 100:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(generate_fibonacci_sequence())

