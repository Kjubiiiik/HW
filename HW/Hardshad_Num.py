#A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.
#Examples
#is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

Num = int(input("Zadejte číslo: "))
def Is_Harshad(Num):
  return Num % sum(int(x) for x in str(Num)) == 0
print(Is_Harshad(Num))