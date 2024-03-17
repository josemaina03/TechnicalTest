#Write a program that counts the number of vowels in a sentence

def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    mySentence = input("Enter a sentence: ")
    num_vowels = count_vowels(mySentence)
    print("Number of vowels:", num_vowels)

main()
