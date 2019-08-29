

#!/usr/bin/python

'''Calling mutli variables
    and
    print functions'''
 
firstname,middlename,lastname,dob = 'Namrata',"Grace","Meripo",3006
print("Firstname %s Middlename %s Lastname %s DOB %d"  %('Namrata','Grace',"Meripo",3006))
print("Firstname %s Lastname %s Middlename %s DOB %d" %(firstname,middlename,lastname,dob))
print("Firstname {} Lastname {} Middlename {} DOB {}" .format("Namrata","Meripo","Grace",3006))
print("Firstname {} Lastname {} Middlename {} DOB {}" .format(firstname,lastname,middlename,dob))
print(f"Firstname {firstname} Lastname {lastname} Middlename {middlename} DOB {dob}")


''' Tuple Index out of range ----- .
format {} are not working in Python -- bug '''
#print("Firstname {3} Lastname {1} Middlename {4} DOB {2}" .format('Namrata',"Meripo","Grace", 3006))











