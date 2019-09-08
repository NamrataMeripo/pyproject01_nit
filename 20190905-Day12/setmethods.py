    #!/usr/bin/python

a = [1,2,3,4,5,1,2,3]
b = [6,7,8,9,1,2,3,4]
'''
# Union values - no duplicates
print(a)
print("")
print(set(a).union(set(b)))
print("")
print(set(b).union(set(a)))
print("")
print(set([1,2,3,4,1,2,3]).union(set([3,4,5,6,3,6,7,8])))
print("")

# insersection values
print(set(a).intersection(set(b)))
print("")

# difference
print(set(a).difference(set(b)))  # 2,5,7,8,9

# update the sets
s = set ([1,2,3,4])
s.update([3,4,5,6])
print(s)
print("")


# add datatype in the sets
s = set ([1,2,3,4])
s.add(5)
print(s)
print("")

# remove the datatype in the sets
r = set([3,4,5,6,7,8,8])
r.remove(8)
print(r)
print("") ' # if element is available , remove ; if element doesnt exists it throws an exception

# discard - if not available in the set, it doesnt throws any exception
r = set([3,4,5,6,7,8,8])
r.discard(1)
print(r)
'''

# pop - It removes the first element
p = set([2,3,4,5,6,])
p.pop()
print(p)



