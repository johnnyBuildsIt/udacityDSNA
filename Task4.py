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
outgoingCalls = set()
incomingCalls = set()
outgoingTexts = set()
incomingTexts = set()

for e in calls:
    outgoingCalls.add(e[0])
    incomingCalls.add(e[1])

for e in texts:
    outgoingTexts.add(e[0])
    incomingTexts.add(e[1])

suspectedTelemarketers = []

for e in outgoingCalls:
    if e not in incomingCalls and e not in outgoingTexts and e not in incomingTexts:
        suspectedTelemarketers.append(e)

print("These numbers could be telemarketers:")
print(*sorted(suspectedTelemarketers), sep='\n')
