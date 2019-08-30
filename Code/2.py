mess = '''
#The mess of stuff from the page source.
'''

elements = []

for element in mess:
    if element == '\n':
        continue
    elif element not in elements:
        elements.append(element)
        counts = mess.count(element)
        print('{} : {}'.format(element,counts))

'''
import re
print(re.compile("[a-zA-Z]").findall(mess))
'''
