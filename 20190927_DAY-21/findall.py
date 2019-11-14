import re

cloudvendors = "aws gcp pcf cloud"

cloudnames = re.findall('gcp',cloudvendors)
print(cloudnames)






