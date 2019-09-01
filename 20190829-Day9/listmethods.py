
"""
1. list()

A list is a mutable sequence of values of any type.

A list with zero elements is called an empty list.

List elements are indexed by sequential integers, starting with zero.

"""


""" Method : list () ---- List is the built in function 
1. int ()
2. float ()
3. complex ()
4. str ()

"""

'''#ListofBanks = [] - Empty list
ListofBanks = ['a','A','%',0,9]
print(ListofBanks)

listofamericabanks = ["BOA","Chase","Fidelity","Union","americanexpress","visa",9,10]
print(listofamericabanks)

# enumerate ---- assigns the S.No's
print(list(enumerate(listofamericabanks)))
print(len(listofamericabanks))
'''

listofamericabanks = ["BOA","Chase","Fidelity","Union","americanexpress","visa",9,10]
print(listofamericabanks,len(listofamericabanks),id(listofamericabanks),type(listofamericabanks))


