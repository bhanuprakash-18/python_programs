"""
Write a python function to identify and return the number name of a given number. The number should be in the range 1 to 1000. If the number is invalid, return -1.

Example:

Sample input        Expected output

1                       one

15                      fifteen

45                      forty five

125                 one hundred and twenty five

999                 nine hundred and ninety nine

1000                one thousand

1211                    -1
"""

single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
two_digits = ["ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]
 
tens_power = ["hundred", "thousand"]
def integer_to_english(number):
    if number== 1000:
        return single_digits[1] + " " + tens_power[1]
    elif number>=0 and number<=9:
        return single_digits[number]
    elif number>=10 and number<=19:
        return two_digits[number%10]
    elif number>=20 and number<=99:
        r = number%10
        n = number-r
        return tens_multiple[n//10] + " " + single_digits[r]
    elif number>=100 and number<=1000:
        r1 = number%100
        n1 = number//100
        r2 = r1%10
        n2 = r1//10
        if number%10 == 0 and number%10 !=0:
            return single_digits[n1] + " " + tens_power[0] + " " + tens_multiple[n2]
        elif number%100 == 0:
            return single_digits[n1] + " " + tens_power[0]
        if r1>=11 and r1<=19:
            return single_digits[n1] + " " + tens_power[0] + " " + "and" + " " + two_digits[r1%10]
        return single_digits[n1] + " " + tens_power[0] + " " + "and" + " " + tens_multiple[n2] + " " + single_digits[r2]
    else:
        return -1
        

number= 1000
print(integer_to_english(number))