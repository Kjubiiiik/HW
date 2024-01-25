#Given an input string, reverse the string word by word.
#Examples
#reverse_words("the sky is blue") ➞ "blue is sky the"
#reverse_words("  hello world!  ") ➞ "world! hello"
#reverse_words("a good   example") ➞ "example good a"

input_string = "Hello world!"
def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    result_string = ' '.join(reversed_words)
    return result_string
print(reverse_words(input_string))