  
#!/usr/bin/python
tup1 = ('python', 'linux', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "A", "B", "C", "E",5,"$"
#tup3 = """A""","""B""","""C""","""E"""
tup4 = 'a', 'b', 'c', 'd'
#tup4 = '''a''', '''b''', '''c''', '''d'''

print(tup1,len(tup1),id(tup1),type(tup1))
print(tup2,len(tup2),id(tup2),type(tup2))
print(tup3,len(tup3),id(tup3),type(tup3))
print("tup4 is :",tup4,len(tup4),id(tup4),type(tup4))

print(tup3[2])
print(tup1[1])
print(tuple(enumerate(tup1)))
print(tup1)