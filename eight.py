'''Write a function, is_prime, that takes an integer and returns True if
the number is prime and False if the number is not prime'''

def is_prime(num):
    if (num == 1):
        return False
    elif (num == 2):
        return True
    else:
        for nums in range(2,num):
            if (num % nums == 0):
                return False
        return True
print(is_prime(2))
print(is_prime(9))