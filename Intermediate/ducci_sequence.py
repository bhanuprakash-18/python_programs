"""
A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, the next list in the sequence is formed by taking the absolute differences of neighboring integers in the previous list.

Start List: [0,653,1854,4063]

Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]

Assumption: The Ducci sequence ends with a list containing 0s and the starting list contains four elements.

Write a python function that takes a starting list of integers and a number ‘n’ as input, and returns the nth element of the Ducci sequence.

Sample Input                        Expected Output

test_list=[0,653,1854,4063]         [548,1008,1854,3410]
n = 1


"""

def ducci_sequence(test_list,n):
    #start writing your code here
    final_list = []
    temp_list1 = test_list
    temp_list2  = []
    while (sum(temp_list2) != 0) or (len(temp_list2) == 0):
        temp_list2 = []
        for i in range(len(test_list)):
            if i != 3:
                temp_list2.append(abs(temp_list1[i+1] - temp_list1[i]))
            elif i ==3:
                temp_list2.append(abs(temp_list1[3] - temp_list1[0]))
        final_list.append(temp_list2)
        temp_list1 = temp_list2
    return final_list[n]
    

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 3)
print(ducci_element)