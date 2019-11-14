import re

cloud_vendors = "aws azure gcp digitalocean ibm"

filter_vendors = re.split("\s",cloud_vendors,4)

print(filter_vendors)

# \s              -- matches a single whitespace character -- space, newline, return, tab
