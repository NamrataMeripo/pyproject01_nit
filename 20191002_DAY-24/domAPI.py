import xml
from xml.dom import minidom

doc = minidom.parse("/Users/keshavkummari/pyproject01_nit/20191002_DAY-24/staff.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

first = doc.getElementsByTagName("staff")

for staff in first:
    sid = staff.getAttribute("id")
    nickname = staff.getElementsByTagName("nickname")[0]
    salary = staff.getElementsByTagName("salary")[0]
    print("id:%s, nickname:%s, salary:%s" %(sid,nickname.firstChild.data,salary.firstChild.data))
    
