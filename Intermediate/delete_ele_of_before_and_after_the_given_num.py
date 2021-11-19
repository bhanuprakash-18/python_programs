"""
Given a list of integers and a number. Write a python function to find and return the sum of the elements of the list. 
Note: Don't add the given number and also the numbers present before and after the given number in the list.

Sample input                            Expected output



list=[1,2,3,4], number=2                    4

list=[1,2,2,3,5,4,2,2,1,2],number=2         5

list=[1,7,3,4,1,7,10,5],number=7            9

list=[1,2,1,2],number=2                     0
"""

#lex_auth_0127136332814499841204

def sum_of_elements(num_list,number):
    del_index = []
    new_list = []
    for i in range(len(num_list)):
        if num_list[i] == number:
            if i > 0:
                del_index.append(i-1)
            del_index.append(i)
            if i<len(num_list):
                del_index.append(i+1)
    for i in range(len(num_list)):
        if i not in del_index:
            new_list.append(num_list[i])
    result_sum = sum(new_list)
    return result_sum
      
num_list=[1, 3, 5, 7, 10, 1, 7, 100]
number= 7
print(sum_of_elements(num_list, number))
