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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def get_unique_numbers(in_list):
    unique_numbers = []
    for entry in in_list:
        calling_num = entry[0]
        receiving_num = entry[1]
        if calling_num not in unique_numbers:
            unique_numbers.append(calling_num)
        if receiving_num not in unique_numbers:
            unique_numbers.append(receiving_num)

    return len(unique_numbers)


uniqueNumbersTotal = 0
uniqueNumbersTotal += get_unique_numbers(texts)
uniqueNumbersTotal += get_unique_numbers(calls)

print("There are {0} different telephone numbers in the records.".format(uniqueNumbersTotal))
