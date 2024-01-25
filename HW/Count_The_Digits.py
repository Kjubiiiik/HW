#Create a function that counts the number of digits in a number.
def count_digits(number):
    # Convert the number to a string and calculate the length
    num_str = str(number)
    num_digits = len(num_str)
    
    return num_digits
print(count_digits(12345))