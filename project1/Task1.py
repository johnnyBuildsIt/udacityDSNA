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
unique_numbers = set()


def add_numbers_to_unique_set(in_list):
    for entry in in_list:
        unique_numbers.add(entry[0])
        unique_numbers.add(entry[1])


add_numbers_to_unique_set(texts)
add_numbers_to_unique_set(calls)

unique_numbers_total = len(unique_numbers)

print("There are {0} different telephone numbers in the records.".format(unique_numbers_total))
