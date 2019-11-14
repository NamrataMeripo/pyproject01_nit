
# 1. Open a File 

# 2. Read or Write to a File (File Operations)

# 3. Close the file 

# Built-In Functions :

# 1. open()
# 2. close()

"""
# Python File Modes:

Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not 
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation.
                If the file already exists, the operation fails.
'a'		Open for appending at the end of the file
                without truncating it. 
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)
"""
openAfile = open('aws.txt','rt')
print(openAfile.read())

openAfile = open('/Users/keshavkummari/pyproject01_nit/20190927_DAY-21/re_split.py','rt')
print(openAfile.read())
