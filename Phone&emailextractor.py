#!usr/bin/python3
# python script for extracting email addresses and phone numbers
import re
import pyperclip

#Find phone number and email numbers from clipboard(copied text)
text_to_search = str(pyperclip.paste())
print("data pasted from clipboard")
#print(text_to_search)
#pattern for phone numbers(i.e pakistan +92-3XX-XXXXXXX e.g +92-320-7684949)
PhonePattern=re.compile(r'''(
            (\+)?                               # for +
            (\d{2}|\(\d{2}\))?                  #international code(92 for pakistan)
            (\s|-|\.)?                          #for space or - or .
            (\d{3}|\(\d{3}\))                   #for 3XX
            (\s|-|\.)?                          #for space or - or .
            (\d{7}|\(\d{7}\))                   #for XXXXXXX                 
            )''', re.VERBOSE)
#email pattern
EmailPattern=re.compile(r'''(
            [a-zA-Z0-9._%&$#+-]+
            @
            [a-zA-Z0-9.-]+
            )''', re.VERBOSE)

Foundmatches = [] # found matches to save in Foundmatches
for groups in PhonePattern.findall(text_to_search):
    PhoneFound = '-'.join([groups[2],groups[4],groups[6]])
    Foundmatches.append((PhoneFound))
for groups in EmailPattern.findall(text_to_search):
    Foundmatches.append(groups)
if len(Foundmatches) > 0:
    pyperclip.copy('\n'.join(Foundmatches))
    print('Copied to clipboard:/n Extracted phone numbers and email address:')
    print('\n'.join(Foundmatches))
else:
    print('No phone numbers or email addresses found.')
