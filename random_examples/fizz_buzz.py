def fizz_buzz(num):
    if (num % 3 == 0) & (num % 5 == 0):
        return("fizz_buzz")

    if num % 3 == 0:
        return"fizz"

    if num % 5 == 0:
        return"buzz"
    return(num)
message = fizz_buzz(30)
print(message)
