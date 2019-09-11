#!/usr/bin/python

'''
def info(arg1,*vartuple) :
    print(arg1)
    for givename in vartuple:
        print("")
        print(givename)
    return

info ('aws','gcp','google','python')
'''

def infoup(*valinfo):
    for upname in valinfo:
        print("")
        print(upname)
    return

infoup('sun','mon','tues','wed')   