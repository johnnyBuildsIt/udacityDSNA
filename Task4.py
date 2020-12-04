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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoingCalls = []
incomingCalls = []
outgoingTexts = []
incomingTexts = []

for e in calls:
    if e[0] not in outgoingCalls:
        outgoingCalls.append(e[0])
    if e[1] not in incomingCalls:
        incomingCalls.append(e[1])

for e in texts:
    if e[0] not in outgoingTexts:
        outgoingTexts.append(e[0])
    if e[1] not in incomingTexts:
        incomingTexts.append(e[1])

suspectedTelemarketers = []

for e in outgoingCalls:
    if e not in incomingCalls and e not in outgoingTexts and e not in incomingTexts and e[0] != '1':
        suspectedTelemarketers.append(e)

print(suspectedTelemarketers)