class p:
    __firstname = 'Guido' # Private variable

    def __init__(self,name,alias):
        self.name = name
        self.__alias = alias
    
    def who(self):
        print(self.__alias)
        print(self.name)
    
    def __foo(self) :
        print("This is a private method")
        self.__foo ()

x = p("Namrata",'NM')
print(x._p__foo())
print(x._p.firstname)