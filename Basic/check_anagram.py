"""
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input and Output

eat, tea

True

backward,drawback

False 
(Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter

True

About, table

False


"""
def check_anagram(data1,data2):
    l1 = list(map(str,data1))
    l2 = list(map(str,data2))
    for i in range(len(l1)):
        l1[i] = l1[i].lower()
    for i in range(len(l2)):
        l2[i] = l2[i].lower()
        
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] in l2 and l2[i] in l1:
                if l1[i] != l2[i]:
                    pass
                else:
                    return False
            else:
                return False
        return True
    else:
        return False


print(check_anagram("eat","tea"))