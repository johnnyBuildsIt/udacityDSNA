"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
bangaloreCalled = []
uniqueCodes = []


def get_code_for_fixed(num):
    return num[1:num.find(')')]


def get_code_for_mobile(num):
    return num[0:num.find(' ')]


def get_phone_code(num):
    if num[0] == '(':
        return get_code_for_fixed(num)
    elif num[0] == '7' or num[0] == '8' or num[0] == '9':
        return get_code_for_mobile(num)
    else:
        return 140


for entry in calls:
    if "(080)" in entry[0]:
        code = get_phone_code(entry[1])
        bangaloreCalled.append(code)
        if code not in uniqueCodes:
            uniqueCodes.append(code)

uniqueCodes.sort()

print("The numbers called by people in Bangalore have codes:")
for e in uniqueCodes:
    print(e)


# Part B
bangalore_to_bangalore_count = 0
for e in bangaloreCalled:
    if e == "080":
        bangalore_to_bangalore_count += 1

percentage = bangalore_to_bangalore_count / len(bangaloreCalled)

print("\n{0} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(percentage))
