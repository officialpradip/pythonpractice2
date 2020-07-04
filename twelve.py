'''Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.'''
def is_palindrome(s):
    if s == s[::-1]:
        print('Supplied word is palindrome')
    else:
        print('Supplied word is not palindrome')
print(is_palindrome('naman'))
