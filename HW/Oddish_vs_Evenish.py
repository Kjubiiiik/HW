#Create a function that determines whether a number is Oddish or Evenish. 
#A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish".
#Otherwise, return "Evenish".
#For example, oddish_or_evenish(121) should return "Evenish", since 1 + 2 + 1 = 4. oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

num = int(input("Zadejte číslo: "))

def oddish_or_evenish(num):
    list_of_digits = [int(i) for i in str(num)]
    if list_of_digits[0] + list_of_digits[1] % 2 == 0:
        return "Evenish"
    elif (list_of_digits[0] + list_of_digits[1]) % 2 != 0:
        return "Oddish"
print(oddish_or_evenish(num))