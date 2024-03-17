#Write a program that accepts a string as input, capitalizes the first letter of each word in the
#string, and then returns the result string

def capitalize_first_letter(sentence):  
    words = sentence.split()  
    capitalized_words = [word[0].upper() + word[1:] for word in words]  
    return ' '.join(capitalized_words)  

def main():  
    my_string = input("Enter a string: ")  
    capitalized_string = capitalize_first_letter(my_string)  
    print("The Capitalized String is:", capitalized_string)  

main()  

