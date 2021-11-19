"""
Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.
"""

#lex_auth_012694465248329728100

def validate_name(name):
    if len(name)!=0 and len(name)<=15:
        if name.isalpha():
            return True
        else:
            return False
    else:
        return False
    #Start writing your code here

def validate_phone_no(phno):
    if phno.isdigit():
        list_phno = list(map(int,phno))
    if phno.isdigit() and len(phno)==10:
        if sum(list_phno)!= int(list_phno[1])*10:
            return True
        else:
            return False
    else:
        return False
    
    #Start writing your code here

def validate_email_id(email_id):
    if (email_id.endswith('.com') and "@" in email_id ) and email_id.count('@')==1:
        domain_names = ['gmail', 'yahoo',  'hotmail']
        temp = email_id.split('.')
        retval = False
        for domain_name in domain_names:
            if temp[0].endswith(domain_name):
                retval = True
        if retval == True:
            return retval
        retval = False
        return retval
    else:
        return False
        
    #Start writing your code here

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    if not validate_name(name):
        print("Invalid Name")
    elif not validate_phone_no(phone_no):
        print("Invalid phone number")
    elif not validate_email_id(email_id):
        print("Invalid email id")
    else:
        print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9988776654", "email_id-tom@dfg@gmail.com")