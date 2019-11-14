import re
cloud_vendors = "aws azure gcp ibm alibaba digitalocean"

check_value = re.match(r'(.*)GCP(.*)',cloud_vendors,re.M|re.I)

if check_value:
    print(check_value.group())
    print(check_value.groups())
else:
    print("No Match!")

# group(num=0)	This method returns entire match (or specific subgroup num)
# groups()	This method returns all matching subgroups in a tuple (empty if there weren't any)