"""
Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and returns the equivalent roman numeral of it.

Sample input            Expected output

1                           I

1796                    MDCCXCVI

4998                    MMMMCMXCVIII

Here are the basics:

I   The easiest way to note down a number is to make that many marks - little I's. Thus I means 1, II means 2, III means 3. However, four strokes seemed like too many....

V   So the Romans moved on to the symbol for 5 - V. Placing I in front of the V — or placing any smaller number in front of any larger number — indicates subtraction. So IV means 4. After V comes a series of additions - VI means 6, VII means 7, VIII means 8.

X   means 10. But wait — what about 9? Same deal. IX means to subtract I from X, leaving 9. Numbers in the teens, twenties and thirties follow the same form as the first set, only with X's indicating the number of tens. So XXXI is 31, and XXIV is 24.

L   means 50. Based on what you've learned, I bet you can figure out what 40 is. If you guessed XL, you're right = 10 subtracted from 50. And thus 60, 70, and 80 are LX, LXX and LXXX.

C   stands for centum, the Latin word for 100. A centurion led 100 men. We still use this in words like "century" and "cent." The subtraction rule means 90 is written as XC. Like the X's and L's, the C's are tacked on to the beginning of numbers to indicate how many hundreds there are: CCCLXIX is 369.

D   stands for 500. As you can probably guess by this time, CD means 400. So CDXLVIII is 448. (See why we switched systems?)

M   is 1,000. You see a lot of Ms because Roman numerals are used a lot to indicate dates. For instance, this page was written in the year of Nova Roma's founding, 1998 CE (Common Era; Christians use AD for Anno Domini, "year of our Lord"). That year is written as MCMXCVIII. But wait! Nova Roma counts years from the founding of Rome, ab urbe condita. By that reckoning Nova Roma was founded in 2751 a.u.c. or MMDCCLI.
"""

def convert_to_roman(num):
    #Start writing your code here
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ["", "C", "CC", "CCC", 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousand = ['', 'M', 'MM', 'MMM', 'MMMM']
    
    if num>=1 and num<=9:
        return ones[num]
    if num>=10 and num<=99:
        if num%10 == 0:
            return tens[num//10]
        else:
            return tens[num//10]+ones[num%10]
    if num>=100 and num<=999:
        if num%100 == 0:
            return hundreds[num//100]
        elif num%10 == 0:
            return hundreds[num//100]+tens[(num%100)//10]
        else:
            return hundreds[num//100]+tens[(num%100)//10]+ones[num%10]
    if num>=1000 and num<=4999:
        if num%1000 == 0:
            return thousand[num//1000]
        elif num%100 == 0:
            return thousand[num//1000] + hundreds[(num%1000)//100]
        elif num%10 == 0:
            return thousand[num//1000] + hundreds[(num%1000)//100] + tens[((num%1000)%100)//10]
        else:
            return thousand[num//1000] + hundreds[(num%1000)//100] + tens[((num%1000)%100)//10] + ones[(((num%1000)%100)%10)]
        

for num in range(1,5000):    
    print(num," : ",convert_to_roman(num))