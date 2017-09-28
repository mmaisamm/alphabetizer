# Program alphabetize a string the user provides

my_string = input("Enter a string of words: ")

# string => list of words
words = my_string.split()

#sort the words
words.sort()

# print  sorted list

print("The sorted words in alphabetical order are as follows:")
for word in words:
   print(word)