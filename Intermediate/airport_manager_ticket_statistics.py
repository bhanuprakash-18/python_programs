"""
Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.

Go through the below program and complete it based on the comments mentioned in it.


Note: Perform case sensitive string comparisons wherever necessary.
"""
#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=['AI101:MUM:LON:001', 'AI102:DEL:LON:002', 'AF005:MUM:LON:067', 'SI456:MUM:SIN:145', 'EM456:MUM:DUB:098', 'AI077:MUM:LON:050', 'EM999:MUM:CAN:051', 'SI123:DEL:SIN:146']
def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count = 0
    for i in ticket_list:
        l = i.split(':')
        
        if l[2]== destination:
            count += 1
    return count
    #Remove pass and write your logic here

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    dictt = {}
    for i in ticket_list:
        l = i.split(":")
        dictt.setdefault(l[0],0)
        dictt[l[0]] += 1
    ls = []
    for key, value in dictt.items():
        s = key+":"+str(value)
        ls.append(s)
    return ls
    #Remove pass and write your logic here

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    ls = find_passengers_per_flight()
    c= []
    t = []
    for i in ls:
        l = i.split(":")
        c.append(l[1])
    c.sort(reverse = True)
    for j in c:
        for i in ls:
            l = i.split(":")
            if j == l[1]:
                s = l[0] + ":" + l[1]
                t.append(s)
            
                
    return t
        
    
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())