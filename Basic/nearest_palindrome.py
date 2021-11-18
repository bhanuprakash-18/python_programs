"""
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 

Sample Input and output:

12300   -   12321

12331   -   12421

"""
#lex_auth_01269443664174284882
def check_palindrome(num):
    n = num
    reverss = 0
    while n!=0:
        r = n%10
        reverss = reverss*10 + r
        n = n//10
    if reverss==num:
        return num
    return "null"


def nearest_palindrome(number):
    n = number+1
    if n>=10:
        while check_palindrome(n) == "null":
            n += 1
            ans = check_palindrome(n)
        return ans
    else:
        return n
    #start writitng your code here

number=12300
print(nearest_palindrome(number))