"""
Problem Description

Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

For example
5 = 2 + 3,
17 = 2 + 3 + 5 + 7,
41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000
"""
#CODE

N = int(input())
p_sum = 0
array = []
prime_sum_count = 0
for i in range(2,N):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count  = count +1
    if count ==0:
        array.append(i)
    
for i in array:
    count = 0
    p_sum = p_sum + i
    if p_sum <= N and p_sum>=3:
        for j in range(2,p_sum):
            if p_sum%j == 0:
                count  = count +1
        if count ==0:
            prime_sum_count = prime_sum_count + 1
print(prime_sum_count)
