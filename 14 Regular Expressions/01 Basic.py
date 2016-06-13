import re

m = re.search('(?<=abc)def', 'abcdef') # start at 'abc' and look for 'def' in 'abcdef'
##print(m.group(0))
##
##
##m = re.search('(?<=-)\w+', 'high-calibre bullet') # start at '-' and get what follows until a space
##print(m.group(0))

##line = "Dr Mark Lee Age 29 01214144765"
##
##book = """Page 26
##Dr Mark Lee Age 29 01214144765
##Mr Mike Leigh Age 43 01212482394
##<deleted>
##Ms Sue Smith Age 21
##"""
##
##m = re.search('\w+\b\w+\b\w+\b\w+\b\d+\b\d+', line)
##print(m.group(0))

phrase = 'MrBond'

m = re.search('(?<=Mr)\w+', phrase)
print(m.group(0))

