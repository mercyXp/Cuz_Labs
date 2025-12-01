# Q.1 Write a Python program to test whether a passed letter is a vowel or not.

vowels = ['a', 'e', 'i', 'o', 'u']

letter = input("Enter any letter of the alphabet: ")

if letter in vowels:
    print("vowel")
else:
    print("not a vowel")

