import os 

import fnmatch 

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']

matches = []

for dirpath,dirnames,filenames in os.walk('/Users/keshavkummari/pyproject01_nit/20191001_DAY-23'):
    for extentions in images:
        for i in fnmatch.filter(filenames,extentions):
            matches.append(os.path.join(dirpath,i))
            print(matches)
            
