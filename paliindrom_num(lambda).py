word = input("Enter a word: ")

# Using lambda to reverse
reverse = lambda x: x[::-1]

print(reverse(word))

if word == reverse(word):
    print("Palindrome")
else:
    print("Not a Palindrome")