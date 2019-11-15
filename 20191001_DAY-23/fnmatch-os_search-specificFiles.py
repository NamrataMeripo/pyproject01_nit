import os 

import fnmatch 

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']

matches = []

for dirpath,dirnames,filenames in os.walk('/c/Python/pyproject01_nit/newpractice'):
    for extentions in images:
        for i in fnmatch.filter(filenames,extentions):
            matches.append(os.path.join(dirpath,i))
            print(matches)
            
