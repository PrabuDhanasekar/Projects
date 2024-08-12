def fizz_buzz(num):
    if(num % 3 == 0 and num %5 == 0):
        return "fizz_buzz"
    elif(num%3 == 0):
        return "fizz"
    elif(num %5 == 0):
        return"buzz"
    else:
        return "Try again"

input = input("Please enter the number:")
input = int(input)
print(fizz_buzz(input))